PROJECT_NAME = backend
DJANGO_PROJECT_NAME = products_prices
PROJECT_SRV = bi_${DJANGO_PROJECT_NAME}_${PROJECT_NAME}

.PHONY = help
.DEFAULT:
	@echo "Usage: "
	@make help

help: ## Show this help.
	# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
run-local: ## Run the project on Dev mode the local OS using Sqlite DB
	@cd backend/source/products_prices/; ./manage.py runserver --settings=products_prices.settings.development_local
build: requirements ## Update requirements.txt, build and start project.
	@docker-compose up --build
djangoshell: ## Access Django shell_plus inside project container.
	@docker-compose run --rm ${PROJECT_NAME} ${DJANGO_PROJECT_NAME}/manage.py shell
lint:  ## Run linting on Project.
	@bash scripts/code-linter.sh
logs: ## Show project container logs in "follow" mode.
	docker logs -f ${PROJECT_SRV}
osshell:  ## Run a OS shell inside project container.
	@docker-compose run ${PROJECT_NAME} bash
start: ## Start project running in containers on a non-detached mode - foreground.
	@docker-compose up
startbg: ## Start project running in containers on detached mode - background.
	@docker-compose up -d
stop: ## Stop the running project.
	@docker-compose stop
requirements: ## Update requirements.txt file
	poetry export -v -o backend/requirements.txt
