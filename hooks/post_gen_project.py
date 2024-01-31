import subprocess
import time
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.text import Text


class PostGenProject:
    def __init__(self, project_slug, github_user):
        self.project_slug = project_slug
        self.github_user = github_user
        self.project_directory = Path.cwd().absolute()
        self.console = Console()

    def remove_folder(self, folder_path: Path) -> None:
        for child in folder_path.iterdir():
            if child.is_file():
                child.unlink()
            else:
                self.remove_folder(child)
        folder_path.rmdir()

    def remove_file(self, file_path: Path) -> None:
        if file_path.exists():
            file_path.unlink()

    def is_docker_installed(self) -> bool:
        try:
            subprocess.run(["docker", "--version"], capture_output=True, check=True)
        except Exception:
            self.console.print("Warning: Docker is not installed.")

    def recursive_removal(self) -> None:
        conditions_and_paths = [
            ("{{ cookiecutter.include_data_folder }}", [self.project_directory / "data"]),
            ("{{ cookiecutter.include_model_folder }}", [self.project_directory / "models"]),
            ("{{ cookiecutter.include_notebook_folder }}", [self.project_directory / "notebooks"]),
            ("{{ cookiecutter.include_docker }}", [self.project_directory / "Dockerfile"]),
            (
                "{{ cookiecutter.include_docs_folder }}",
                [
                    self.project_directory / "docs",
                    self.project_directory / "mkdocs.yml",
                    self.project_directory / "CHANGELOG.md",
                    self.project_directory / ".github" / "workflows" / "mkdocs.yml",
                ],
            ),
        ]

        if "{{ cookiecutter.include_docker }}" == "True":
            self.is_docker_installed()

        for condition, paths in conditions_and_paths:
            if condition == "False":
                for path in paths:
                    if path.exists():
                        if path.is_dir():
                            self.console.print(Text(f"Removing folder: {path}", "blue"))
                            self.remove_folder(path)
                        elif path.is_file():
                            self.console.print(Text(f"Removing file: {path}", "blue"))
                            self.remove_file(path)

    def print_further_instructions(self) -> None:
        github_message = f"""   Upload initial code to GitHub:
            $ git init
            $ git add .
            $ git commit -m ":tada: Initial commit"
            $ git branch -M main
            $ git remote add origin https://github.com/{self.github_user}/{self.project_slug}.git
            $ git push -u origin main

        or just run:
            $ make connect_to_repo
        """

        text_title = Text.assemble("\n", (f"Project: {self.project_slug} was successfully created", "bold blue"))
        text_caption = Text.assemble(("Happy coding! :)", "bold blue"), "\n")

        table = Table(title=text_title, caption=text_caption)

        table.add_column("Task", style="green", no_wrap=True)
        table.add_column("Commands", style="blue")

        table.add_row("GitHub", github_message)
        table.add_row(f"Move in to project: {self.project_slug}", f"  $ cd {self.project_slug}")
        table.add_row("Configuring poetry for venv", "  $ poetry config --local virtualenvs.in-project true")
        table.add_row("Installing project dependencies with poetry", "  $ poetry install --quiet")
        table.add_row("Activate venv", "    $ poetry shell")

        self.console.print(table)

    def run_command(self, command: list[str], description: str) -> None:
        text_command = Text(description, "blue")
        self.console.print(text_command)
        subprocess.run(command, check=True)

    def running_pre_installation(self) -> None:
        commands = [(["pip", "install", "--quiet", "--upgrade", "pip", "poetry"], "Upgrading pip, installing poetry")]

        for command, description in commands:
            self.run_command(command, description)

    def setup(self):
        with self.console.status("First removing unwanted folders and files..", spinner="dots"):
            time.sleep(0.5)
            self.console.print(Text(""))
            self.recursive_removal()

        with self.console.status("Installing stuff..", spinner="dots"):
            self.console.print(Text(""))
            self.running_pre_installation()

        self.print_further_instructions()


if __name__ == "__main__":
    project_slug = "{{ cookiecutter.project_slug }}"
    github_user = "{{ cookiecutter.github_username }}"
    setup = PostGenProject(project_slug, github_user)
    setup.setup()
