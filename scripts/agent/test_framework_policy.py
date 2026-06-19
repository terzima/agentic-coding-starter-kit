#!/usr/bin/env python3
"""Framework policy smoke tests using only the Python standard library."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_SCRIPT_FILES = {
    "scripts/agent/README.md",
    "scripts/agent/agent_finalize.sh",
    "scripts/agent/agent_preflight.sh",
    "scripts/agent/check_change_control.sh",
    "scripts/agent/filter_output.py",
    "scripts/agent/install_git_hooks.sh",
    "scripts/agent/new_agent_task.sh",
    "scripts/agent/policy_lib.py",
    "scripts/agent/run_framework_checks.sh",
    "scripts/agent/test_framework_policy.py",
}
REMOVED_SCRIPT_FILES = {
    "scripts/agent/" + "policy_" + "check.py",
    "scripts/agent/" + "seed_large_" + "spec.sh",
}
HOOK_FILES = (
    ".githooks/commit-msg",
    ".githooks/pre-commit",
    ".githooks/pre-push",
)
ALLOWED_SAMPLE_FILES = ("." + "env.example",)
REJECTED_SECRET_FILE_CASES = (
    "." + "env",
    "." + "env.local",
    "." + "env.production",
    "nested/." + "env.example",
    "deploy." + "pem",
    "deploy." + "key",
    "id_rsa",
    "id_ed25519",
)


def run_pre_push(remote_ref: str) -> subprocess.CompletedProcess[str]:
    payload = f"refs/heads/codex/test 0000000000000000000000000000000000000000 {remote_ref} 0000000000000000000000000000000000000000\n"
    return subprocess.run(
        [str(ROOT / ".githooks" / "pre-push")],
        input=payload,
        text=True,
        capture_output=True,
        cwd=ROOT,
        check=False,
    )


def current_branch_name(env: dict[str, str] | None = None) -> str:
    result = subprocess.run(
        ["git", "symbolic-ref", "--short", "HEAD"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        env=env,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def assert_remote_ref_policy() -> None:
    for ref in ("refs/heads/main", "refs/heads/master", "refs/heads/release/test"):
        result = run_pre_push(ref)
        assert result.returncode != 0, f"{ref} should be blocked"
        assert "protected remote branch" in result.stderr

    current_branch = current_branch_name()
    result = run_pre_push("refs/heads/codex/test")
    if current_branch in {"main", "master", "prod", "production"} or current_branch.startswith("release/"):
        assert result.returncode != 0
    else:
        assert result.returncode == 0, result.stderr


def assert_remote_ref_policy_handles_detached_head() -> None:
    # GitHub Actions checks out pull requests in detached HEAD mode.
    with tempfile.TemporaryDirectory() as temp_dir:
        fake_bin = Path(temp_dir) / "git"
        fake_bin.write_text(
            "#!/usr/bin/env bash\n"
            "if [ \"$1\" = \"symbolic-ref\" ]; then exit 128; fi\n"
            "command git \"$@\"\n",
            encoding="utf-8",
        )
        fake_bin.chmod(0o755)
        env = os.environ.copy()
        env["PATH"] = f"{temp_dir}:{env['PATH']}"
        assert current_branch_name(env=env) == ""


def run_change_control(changed_files: list[str]) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as temp_dir:
        fake_bin = Path(temp_dir) / "git"
        fake_bin.write_text(
            "#!/usr/bin/env bash\n"
            "if [ \"$1\" = \"rev-parse\" ]; then exit 1; fi\n"
            "if [ \"$1\" = \"ls-files\" ]; then\n"
            + "".join(f"printf '%s\\n' {name!r}\n" for name in changed_files)
            + "exit 0\nfi\n"
            "if [ \"$1\" = \"diff\" ]; then exit 0; fi\n"
            "command git \"$@\"\n",
            encoding="utf-8",
        )
        fake_bin.chmod(0o755)
        env = os.environ.copy()
        env["PATH"] = f"{temp_dir}:{env['PATH']}"
        return subprocess.run(
            ["bash", str(ROOT / "scripts" / "agent" / "check_change_control.sh")],
            text=True,
            capture_output=True,
            cwd=ROOT,
            env=env,
            check=False,
        )


def run_pre_commit(staged_files: list[str]) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as temp_dir:
        fake_bin = Path(temp_dir) / "git"
        fake_bin.write_text(
            "#!/usr/bin/env bash\n"
            "if [ \"$1\" = \"diff\" ] && [ \"$2\" = \"--cached\" ] && [ \"$3\" = \"--name-only\" ]; then\n"
            + "".join(f"printf '%s\\n' {name!r}\n" for name in staged_files)
            + "exit 0\nfi\n"
            "if [ \"$1\" = \"diff\" ] && [ \"$2\" = \"--cached\" ]; then exit 0; fi\n"
            "command git \"$@\"\n",
            encoding="utf-8",
        )
        fake_bin.chmod(0o755)
        env = os.environ.copy()
        env["PATH"] = f"{temp_dir}:{env['PATH']}"
        return subprocess.run(
            ["bash", str(ROOT / ".githooks" / "pre-commit")],
            text=True,
            capture_output=True,
            cwd=ROOT,
            env=env,
            check=False,
        )


def assert_sensitive_file_policy() -> None:
    for sample in ALLOWED_SAMPLE_FILES:
        assert run_change_control([sample]).returncode == 0, sample
        assert run_pre_commit([sample]).returncode == 0, sample

    for secret_file in REJECTED_SECRET_FILE_CASES:
        change_control = run_change_control([secret_file])
        assert change_control.returncode != 0, secret_file
        assert "likely secret file included" in change_control.stderr, secret_file

        pre_commit = run_pre_commit([secret_file])
        assert pre_commit.returncode != 0, secret_file
        assert "likely secret file" in pre_commit.stderr, secret_file


def assert_hook_files_are_executable() -> None:
    for hook in HOOK_FILES:
        path = ROOT / hook
        assert path.exists(), f"missing hook: {hook}"
        assert os.access(path, os.X_OK), f"hook is not executable: {hook}"


def assert_codeowners_has_no_active_placeholder() -> None:
    codeowners = (ROOT / ".github" / "CODEOWNERS").read_text(encoding="utf-8")
    active_lines = [
        line
        for line in codeowners.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    assert not any("@your-github-username" in line for line in active_lines)


def assert_dependency_review_is_manual_only() -> None:
    workflow = (
        ROOT / ".github" / "workflows" / "dependency-review.yml"
    ).read_text(encoding="utf-8")
    assert "pull_request:" not in workflow
    assert "workflow_dispatch:" in workflow


def assert_script_inventory() -> None:
    existing_tracked = {
        line.strip()
        for line in subprocess.check_output(
            ["git", "ls-files", "scripts/agent"],
            cwd=ROOT,
            text=True,
        ).splitlines()
        if line.strip() and (ROOT / line.strip()).exists()
    }
    existing_untracked = {
        line.strip()
        for line in subprocess.check_output(
            ["git", "ls-files", "--others", "--exclude-standard", "scripts/agent"],
            cwd=ROOT,
            text=True,
        ).splitlines()
        if line.strip()
    }
    actual = existing_tracked | existing_untracked

    assert actual == EXPECTED_SCRIPT_FILES, f"script inventory mismatch: {sorted(actual)}"
    for removed in REMOVED_SCRIPT_FILES:
        assert not (ROOT / removed).exists(), f"removed script still exists: {removed}"


def assert_script_docs_cover_inventory() -> None:
    readme = (ROOT / "scripts" / "agent" / "README.md").read_text(encoding="utf-8")
    for script in EXPECTED_SCRIPT_FILES:
        name = Path(script).name
        assert name in readme, f"{name} missing from scripts/agent/README.md"

    for removed in REMOVED_SCRIPT_FILES:
        name = Path(removed).name
        assert name in readme, f"{name} missing from removed/folded script notes"


def assert_framework_checks_are_current() -> None:
    checks = (ROOT / "scripts" / "agent" / "run_framework_checks.sh").read_text(encoding="utf-8")
    for stale in ("SPEC-0007", "PLAN-0007"):
        assert stale not in checks, f"stale framework check target remains: {stale}"
    assert "docs/status/_template.md" in checks
    assert "docs/handoff/_template.md" in checks
    assert "docs/status/CURRENT_STATE.md" not in checks, \
        "starter-kit default checks should not require project CURRENT_STATE.md"


def assert_makefile_does_not_call_removed_scripts() -> None:
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    for removed in REMOVED_SCRIPT_FILES:
        name = Path(removed).name
        assert name not in makefile, f"Makefile still invokes removed script: {name}"
    removed_target = "seed" + "-spec"
    assert removed_target not in makefile, "Makefile still exposes removed seed target"


def assert_policy_lib_at_shared_location() -> None:
    import importlib.util
    lib_path = ROOT / "scripts" / "agent" / "policy_lib.py"
    assert lib_path.exists(), "scripts/agent/policy_lib.py not found"
    spec = importlib.util.spec_from_file_location("policy_lib", lib_path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    for name in ("classify_command", "DENY_PATTERNS", "ASK_PATTERNS", "emit", "load_stdin_json"):
        assert hasattr(module, name), f"policy_lib missing export: {name}"
    assert not (ROOT / ".codex" / "hooks" / "policy_lib.py").exists(), \
        ".codex/hooks/policy_lib.py still exists; should have been moved to scripts/agent/"


def assert_hook_import_resolution() -> None:
    for hook_path in (".codex/hooks/pre_tool_use_policy.py", ".claude/hooks/pre_tool_use_policy.py"):
        result = subprocess.run(
            [sys.executable, str(ROOT / hook_path)],
            input="{}",
            text=True,
            capture_output=True,
            cwd=ROOT,
            check=False,
        )
        assert result.returncode == 0, f"{hook_path} exited {result.returncode}: {result.stderr}"
        assert result.stdout.strip() == "{}", f"{hook_path} unexpected output: {result.stdout!r}"

    deny_input = '{"tool_input": {"command": "sudo rm -rf /"}}'
    for hook_path in (".codex/hooks/pre_tool_use_policy.py", ".claude/hooks/pre_tool_use_policy.py"):
        result = subprocess.run(
            [sys.executable, str(ROOT / hook_path)],
            input=deny_input,
            text=True,
            capture_output=True,
            cwd=ROOT,
            check=False,
        )
        assert result.returncode == 0, f"{hook_path} crashed on deny input: {result.stderr}"
        import json as _json
        out = _json.loads(result.stdout)
        decision = out.get("hookSpecificOutput", {}).get("permissionDecision")
        assert decision == "deny", f"{hook_path} expected deny, got: {result.stdout!r}"


def main() -> int:
    assert_policy_lib_at_shared_location()
    assert_hook_import_resolution()
    assert_script_inventory()
    assert_script_docs_cover_inventory()
    assert_framework_checks_are_current()
    assert_makefile_does_not_call_removed_scripts()
    assert_hook_files_are_executable()
    assert_remote_ref_policy_handles_detached_head()
    assert_remote_ref_policy()
    assert_sensitive_file_policy()
    assert_codeowners_has_no_active_placeholder()
    assert_dependency_review_is_manual_only()
    print("framework policy checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
