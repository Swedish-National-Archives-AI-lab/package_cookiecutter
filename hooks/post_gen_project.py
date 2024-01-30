import subprocess
import textwrap
from pathlib import Path


# Project root directory
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
GITHUB_USER = "{{ cookiecutter.github_username }}"

PROJECT_DIRECTORY = Path.cwd().absolute()


def remove_folder(folder_path: Path) -> None:
    for child in folder_path.iterdir():
        print(child)
        if child.is_file():
            child.unlink()
        else:
            remove_folder(child)
    folder_path.rmdir()


def remove_file(file_path: Path) -> None:
    if file_path.exists():
        print(file_path)
        file_path.unlink()


# def recursive_removal() -> None:
#     removal_conditions = {
#         "{{ cookiecutter.include_data_folder }}": [PROJECT_DIRECTORY / "data"],
#         "{{ cookiecutter.include_model_folder }}": [PROJECT_DIRECTORY / "model"],
#         "{{ cookiecutter.include_notebook_folder }}": [PROJECT_DIRECTORY / "notebooks"],
#         "{{ cookiecutter.include_docker }}": [PROJECT_DIRECTORY / "Dockerfile"],
#         "{{ cookiecutter.include_docs_folder }}": [
#             PROJECT_DIRECTORY / "docs",
#             PROJECT_DIRECTORY / "mkdocs.yml",
#             PROJECT_DIRECTORY / "CHANGELOG.md",
#             PROJECT_DIRECTORY / ".github" / "workflows" / "mkdocs.yml",
#         ],
#     }

#     for condition, paths in removal_conditions.items():
#         if condition != "y":
#             for path in paths:
#                 print(f"Removing: {path}")
#                 if path.is_dir():
#                     remove_folder(path)
#                 elif path.is_file():
#                     remove_file(path)


def recursive_removal() -> None:
    if "{{ cookiecutter.include_data_folder }}" != "y":
        data_folder = PROJECT_DIRECTORY / "data"
        if data_folder.exists():
            remove_folder(data_folder)

    if "{{ cookiecutter.include_model_folder }}" != "y":
        model_folder = PROJECT_DIRECTORY / "models"
        if model_folder.exists():
            remove_folder(model_folder)

    if "{{ cookiecutter.include_notebook_folder }}" != "y":
        notebook_folder = PROJECT_DIRECTORY / "notebooks"
        if notebook_folder.exists():
            remove_folder(notebook_folder)

    if "{{ cookiecutter.include_docker }}" != "y":
        docker_file = PROJECT_DIRECTORY / "Dockerfile"
        if docker_file.exists():
            remove_file(docker_file)

    if "{{ cookiecutter.include_docs_folder }}" != "y":
        docs_folder = PROJECT_DIRECTORY / "docs"
        if docs_folder.exists():
            remove_folder(docs_folder)
        mkdocs_file = PROJECT_DIRECTORY / "mkdocs.yml"
        if mkdocs_file.exists():
            remove_file(mkdocs_file)
        changelog_file = PROJECT_DIRECTORY / "CHANGELOG.md"
        if changelog_file.exists():
            remove_file(changelog_file)
        mkdocs_workflow = PROJECT_DIRECTORY / ".github" / "workflows" / "mkdocs.yml"
        if mkdocs_workflow.exists():
            remove_folder(mkdocs_workflow)


def print_futher_instuctions(project_slug: str, github: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_slug: current project name
        github: GitHub username
    """
    message = f"""
    ################ Project successfully initialized ################

    Your project {project_slug} was created.

    1. Upload initial code to GitHub:

        $ git init
        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{github}/{project_slug}.git
        $ git push -u origin main

    or just run:
        make connect_to_repo

    2.

    To activate venv run:
        $ poetry shell

    This will activate the local virtual environment with poetry shell.

    ############################################################

    Happy Coding :)


    """
    print(textwrap.dedent(message))


def run_command(command: list[str], description: str) -> None:
    print(f"Running '{' '.join(command)}'")
    subprocess.run(command, check=True)


def running_pre_installation() -> None:
    # (shell command , msg )
    commands = [
        (["pip", "install", "--upgrade", "pip", "poetry"], "upgrading pip, installing poetry"),
        (["pre-commit", "install"], "installing pre-commit hooks"),
        (
            ["poetry", "config", "--local", "virtualenvs.in-project", "true"],
            "configuring poetry for local virtual environments",
        ),
        (["poetry", "install"], "installing project dependencies with poetry"),
    ]

    for command, description in commands:
        run_command(command, description)


def main() -> None:
    print("First removing unwanted folders and files..")
    recursive_removal()

    # print("Installing stuff..")
    # running_pre_installation()

    # print_futher_instuctions(project_slug=PROJECT_SLUG, github=GITHUB_USER)


if __name__ == "__main__":
    main()
