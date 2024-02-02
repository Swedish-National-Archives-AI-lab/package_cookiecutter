include .env

REPO_URL = https://{{cookiecutter.github_username}}/{{ cookiecutter.project_slug }}
PACKAGE = {{cookiecutter.package_name}}

## help - Display this help screen
help:
	@grep -h "##" $(MAKEFILE_LIST) | grep -v grep | sed -e 's/\\$$//' -e 's/##//'

## connect_to_repo - Connects local repo to github repo with the same name as the repo locally
connect_to_repo:
	git init .
	git add --all
	git commit -m "First commit.."
	git branch -M main
	git remote add origin $(REPO_URL)
	git push -u origin main

## configure_startup - Configuring poetry for venv + Installing project dependencies with poetry + Activate venv
configure_startup:
	pip install --quiet --upgrade pip poetry
	poetry config --local virtualenvs.in-project true
	poetry install --quiet
	poetry shell

	@echo Don't forget to push changes..


magic: connect_to_repo configure_startup

## release - Release a new version
release:
	@echo git tag -a "vX.Y.Z" -m "Release X.Y.Z"
	@echo git push origin vX.Y.Z
	@echo change release vX.Y.Z in setup.py..

## pre_commit - Setup pre-commit hooks
pre_commit:
	pre-commit --version
	pre-commit install
	pre-commit run

## local_clean_windows - Clean local folders for windows
local_clean_windows:
	if exist "dist" rmdir /S dist
	if exist ".pytest_cache" rmdir /S .pytest_cache
	if exist ".mypy_cache" rmdir /S .mypy_cache
	if exist ".tox" rmdir /S .tox
	if exist "src\${PACKAGE}.egg-info" rmdir /S src\${PACKAGE}.egg-info
	if exist "src\${PACKAGE}\__pycache__" rmdir /S src\${PACKAGE}\__pycache__
	if exist "tests\unit\__pycache__" rmdir /S tests\unit\__pycache__
	if exist ".coverage" del .coverage

## local_clean_linux - Clean local folders for linux
local_clean_linux:
	rm -r dist
	rm -r .pytest_cache
	rm -r .mypy_cache
	rm -r .tox
	rm -r src/${PACKAGE}.egg-info
	rm -r src/${PACKAGE}/__pycache__
	rm -r tests/unit/__pycache__
	rm .coverage

## docker_build - Build and run docker container
docker_build:
	docker build -t ${PACKAGE} .
	docker run ${PACKAGE}


