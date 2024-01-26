import subprocess
import textwrap
from pathlib import Path

# Project root directory
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
GITHUB_USER = "{{ cookiecutter.github_name }}"

PROJECT_DIRECTORY = Path.cwd().absolute()


def remove_folder(folder_path: str) -> None:
    for child in folder_path.iterdir(): 
        if child.is_file():
            child.unlink() 
        else:
            remove_folder(child)  
    folder_path.rmdir()  

def remove_file(file_path: str) -> None:
    if file_path.exists():
        file_path.unlink()

def recursive_removal() -> None:
    removal_conditions = {
        'include_data_folder': [PROJECT_DIRECTORY / 'data'],
        'include_model_folder': [PROJECT_DIRECTORY / 'model'],
        'include_docker': [PROJECT_DIRECTORY / 'Dockerfile.'],
        'include_notebook_folder': [PROJECT_DIRECTORY / 'notebooks'],
        'include_docs_folder': [
            PROJECT_DIRECTORY / 'docs',
            PROJECT_DIRECTORY / 'mkdocs.yml',
            PROJECT_DIRECTORY / 'CHANGELOG.MD',
            PROJECT_DIRECTORY / '.github' / 'workflows' / 'mkdocs.yml'
        ],
    }

    for condition, paths in removal_conditions.items():
        if '{{ cookiecutter.' + condition + ' }}' != 'y':
            for path in paths:
                if path.is_dir():
                    remove_folder(path)
                elif path.is_file():
                    remove_file(path)


def print_futher_instuctions(project_name: str, github: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_name: current project name
        github: GitHub username
    """
    message = f"""
    Your project {project_name} is created.
    
    Upload initial code to GitHub:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{github}/{project_name}.git
        $ git push -u origin main

    or just run:
        make connect_to_repo
    """
    print(textwrap.dedent(message))

def run_command(command: list[str], description: str) -> None:
    print(f"Running '{' '.join(command)}'")
    subprocess.run(command, check=True)

def run_poetry_pre_commit() -> None:

    # (shell command , msg )
    commands = [
        (['pip', 'install', '--upgrade', 'pip', 'pre-commit', 'poetry'], "upgrading pip, installing pre-commit and poetry"),
        (['pre-commit', 'install'], "installing pre-commit hooks"),
        (['poetry', 'config', '--local', 'virtualenvs.in-project', 'true'], "configuring poetry for local virtual environments"),
        (['poetry', 'install'], "installing project dependencies with poetry"),
        (['poetry', 'shell'], "activating local virtual environment with poetry shell")
    ]

    for command, description in commands:
        run_command(command, description)


def main() -> None:

    print("First removing unwanted folders and files..")
    recursive_removal()

    print("Running 'git init'")
    subprocess.run(['git', 'init'], check=True)

    run_poetry_pre_commit()

    print("################ Project successfully initialized ################")

    print_futher_instuctions(project_name=PROJECT_NAME, github=GITHUB_USER)


if __name__ == "__main__":
    main()
