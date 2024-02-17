#
# environment
#
SHELL := /bin/bash
APPNAME := app
CONTAINER_IMAGE_NAME_PROD := ${APPNAME}-prod
PYTHON_VERSION := 3.12.1
PYTHON_VENV := venv
APPFOLDER := app

#
# includes
#
include makefiles/*

#
# help
#
help: help_python help_git help_docker_base
	@echo ""
	@echo "------------------------ Configmaster --------------------------------"
	@echo "make setup -------------------- Setup the whole project for development"
	@echo "make setupdb ------------------ Setup development database"
	@echo "make run-dev ------------------ Run the development environment in docker"
	@echo ""
	@echo "-------------------- Django: Common Tasks ----------------------------"
	@echo "make migrations --------------- Create database migrations"
	@echo "make migrate ------------------ Apply database migrations"
	@echo ""
	@echo "-------------------- Docker: Project secific ----------------------"
	@echo "make run-dev ------------------ Run the dev build"
	@echo "make run-prod ----------------- Run the prod build"
	@echo "make run-test ----------------- Run the test build"
	@echo "make run-local ---------------- Run the dev build outside of container"
	@echo "make rootshell ---------------- Run a root shell in prod container"
	@echo "make shell -------------------- Run a shell in prod container"
	@echo ""

#
# configmaster targets
#
clean:
	@find . -type d -name "__pycache__" -prune -exec rm -rf "{}" \;
	@rm -rf \
		.mypy_cache/ \
		.pytest_cache/ \
		cov/
	@find . -type d -name "__pycache__" -prune -exec rm -rf "{}" \;

setup: venv-install setupdb
	@echo "executing target setup"

setupdb:
	@echo "executing target setupdb"
	@echo "some postgres voodoo here"

run-dev:
	@echo "executing target run-dev"
	@echo "some docker-compose voodoo here"

#
# docker run targets


run-local:
	@echo "executing target run-local"
	# Run environment
	docker compose down --volumes
	docker compose up --build

#
# docker shell targets
#
shell:
	@echo "executing target shell"
	@$ docker compose exec -it \
		app \
		${SHELL}

rootshell:
	@echo "executing target rootshell"
	@$ docker compose exec -it \
		--user root \
		app \
		${SHELL}
