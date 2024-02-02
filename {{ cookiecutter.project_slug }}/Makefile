include .env

REPO_URL = https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug }}
PACKAGE = {{cookiecutter.package_name}}

## help - Display this help screen in a more structured format
help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


connect_to_repo: ## connect_to_repo - Connects local repo to github repo with the same name as the repo locally
	git init .
	git add --all
	git commit -m "First commit.."
	git branch -M main
	git remote add origin $(REPO_URL)
	git push -u origin main

configure_startup: ## configure_startup - Configuring poetry for venv + Installing project dependencies with poetry + Activate venv
	pip install --quiet --upgrade pip poetry
	poetry config --local virtualenvs.in-project true
	poetry install --quiet
	poetry shell

	@echo Don't forget to push changes..


magic: connect_to_repo configure_startup ## runs connect_to_repo & configure_startup


release: ## release - Release a new version
	@echo git tag -a "vX.Y.Z" -m "Release X.Y.Z"
	@echo git push origin vX.Y.Z
	@echo change release vX.Y.Z in setup.py..


pre_commit: ## pre_commit - Setup pre-commit hooks
	pre-commit --version
	pre-commit install
	pre-commit run

local_clean_windows: ## local_clean_windows - Clean local folders for windows
	if exist "dist" rmdir /S dist
	if exist ".pytest_cache" rmdir /S .pytest_cache
	if exist ".mypy_cache" rmdir /S .mypy_cache
	if exist ".tox" rmdir /S .tox
	if exist "src\${PACKAGE}.egg-info" rmdir /S src\${PACKAGE}.egg-info
	if exist "src\${PACKAGE}\__pycache__" rmdir /S src\${PACKAGE}\__pycache__
	if exist "tests\unit\__pycache__" rmdir /S tests\unit\__pycache__
	if exist ".coverage" del .coverage

local_clean_linux: ## local_clean_linux - Clean local folders for linux
	rm -r dist
	rm -r .pytest_cache
	rm -r .mypy_cache
	rm -r .tox
	rm -r src/${PACKAGE}.egg-info
	rm -r src/${PACKAGE}/__pycache__
	rm -r tests/unit/__pycache__
	rm .coverage

docker_build: ## docker_build - Build and run docker container
	docker build -t ${PACKAGE} .
	docker run ${PACKAGE}