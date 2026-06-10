.PHONY: install-hooks preflight finalize new-task seed-spec

install-hooks:
	./scripts/agent/install_git_hooks.sh

preflight:
	./scripts/agent/agent_preflight.sh

finalize:
	./scripts/agent/agent_finalize.sh

new-task:
	@if [ -z "$(TASK)" ] || [ -z "$(SLUG)" ]; then echo "Usage: make new-task TASK=0001 SLUG=short-name"; exit 2; fi
	./scripts/agent/new_agent_task.sh $(TASK) $(SLUG)

seed-spec:
	./scripts/agent/seed_large_spec.sh
