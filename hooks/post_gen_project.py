import subprocess
import time
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.text import Text


# Project root directory
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
GITHUB_USER = "{{ cookiecutter.github_username }}"

PROJECT_DIRECTORY = Path.cwd().absolute()


def remove_folder(folder_path: Path) -> None:
    for child in folder_path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            remove_folder(child)
    folder_path.rmdir()


def remove_file(file_path: Path) -> None:
    if file_path.exists():
        file_path.unlink()


def recursive_removal(console: Console) -> None:
    conditions_and_paths = [
        ("{{ cookiecutter.include_data_folder }}", [PROJECT_DIRECTORY / "data"]),
        ("{{ cookiecutter.include_model_folder }}", [PROJECT_DIRECTORY / "models"]),
        ("{{ cookiecutter.include_notebook_folder }}", [PROJECT_DIRECTORY / "notebooks"]),
        ("{{ cookiecutter.include_docker }}", [PROJECT_DIRECTORY / "Dockerfile"]),
        (
            "{{ cookiecutter.include_docs_folder }}",
            [
                PROJECT_DIRECTORY / "docs",
                PROJECT_DIRECTORY / "mkdocs.yml",
                PROJECT_DIRECTORY / "CHANGELOG.md",
                PROJECT_DIRECTORY / ".github" / "workflows" / "mkdocs.yml",
            ],
        ),
    ]

    for condition, paths in conditions_and_paths:
        print(condition)
        if not condition:
            for path in paths:
                if path.exists():
                    if path.is_dir():
                        console.print(Text(f"Removing folder:{path}", "blue"))
                        remove_folder(path)
                    elif path.is_file():
                        console.print(Text(f"Removing folder:{path}", "blue"))
                        remove_file(path)


def print_futher_instuctions(console: Console, project_slug: str, github: str) -> None:
    github_message = f"""   Upload initial code to GitHub:
        $ git init
        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{github}/{project_slug}.git
        $ git push -u origin main

    or just run:
        $ make connect_to_repo
    """

    text_title = Text.assemble("\n", ("Project: {project_slug} was successfully created", "bold blue"))
    text_caption = Text.assemble(("Happy coding! :)", "bold blue"), "\n")

    table = Table(title=text_title, caption=text_caption)

    table.add_column("Task", style="green", no_wrap=True)
    table.add_column("Commands", style="blue")

    table.add_row("GitHub", github_message)
    table.add_row("Activate venv", "    $ poetry shell")

    console.print(table)


def run_command(command: list[str], description: str, console: Console) -> None:
    text_command = Text(f"Running '{' '.join(command)}'", "blue")
    console.print(text_command)
    subprocess.run(command, check=True)


def running_pre_installation(console: Console) -> None:
    commands = [
        (["pip", "install", "--quiet", "--upgrade", "pip", "poetry"], "upgrading pip, installing poetry"),
        (
            ["poetry", "config", "--local", "virtualenvs.in-project", "true"],
            "configuring poetry for local virtual environments",
        ),
        (["poetry", "install", "--quiet"], "installing project dependencies with poetry"),
    ]

    for command, description in commands:
        run_command(command, description, console)


def main() -> None:
    console = Console()
    console.print(Text(""))

    with console.status("First removing unwanted folders and files..", spinner="dots"):
        time.sleep(0.5)
        recursive_removal(console)

    with console.status("Installing stuff..", spinner="dots"):
        running_pre_installation(console)

    print_futher_instuctions(console, project_slug=PROJECT_SLUG, github=GITHUB_USER)


if __name__ == "__main__":
    main()
