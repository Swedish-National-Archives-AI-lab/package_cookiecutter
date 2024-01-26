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
    removal_map = {
        'include_data_folder': PROJECT_DIRECTORY / 'data',
        'include_model_folder': PROJECT_DIRECTORY / 'model',
        'include_notebook_folder': PROJECT_DIRECTORY / 'notebooks',
        'include_docs_folder': PROJECT_DIRECTORY / 'notebooks',
        'include_docs_folder': PROJECT_DIRECTORY / 'mkdocs.yml',
        'include_docs_folder': PROJECT_DIRECTORY / 'CHANGELOG.MD',
        'include_docs_folder': PROJECT_DIRECTORY / '.github' / 'workflows' /'mkdocs.yml'
    }

    for key, path in removal_map.items():
        if '{{ cookiecutter.' + key + ' }}' != 'y':
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
    """
    print(textwrap.dedent(message))

def run_poetry_pre_commit() -> None:

    print("Running 'pip install --upgrade pip pre-commit poetry'")
    subprocess.run(['pip', 'install', '--upgrade', 'pip', 'pre-commit', 'poetry'], check=True)

    print("Running 'pre-commit install'")

    subprocess.run(['pre-commit', 'install'], check=True)

    print("Running 'poetry config --local virtualenvs.in-project true'")
    subprocess.run(['poetry', 'config', '--local', 'virtualenvs.in-project', 'true'], check=True)

    print("Running 'poetry install'")
    subprocess.run(['poetry', 'install'], check=True)


def main() -> None:

    print("First removing unwanted folders and files..")
    recursive_removal()

    print("Running 'git init'")
    subprocess.run(['git', 'init'], check=True)

    run_poetry_pre_commit()

    print("Project successfully initialized")

    print_futher_instuctions(project_name=PROJECT_NAME, github=GITHUB_USER)


if __name__ == "__main__":
    main()
