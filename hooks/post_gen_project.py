import subprocess
from pathlib import Path

import toml
from rich.console import Console
from rich.table import Table
from rich.text import Text


class PostGenProject:
    def __init__(self, project_slug, github_user):
        self.project_slug = project_slug
        self.github_user = github_user
        self.project_directory = Path.cwd().absolute()
        self.console = Console()

    def _remove_folder(self, folder_path: Path) -> None:
        for child in folder_path.iterdir():
            if child.is_file():
                child.unlink()
            else:
                self._remove_folder(child)
        folder_path.rmdir()

    def _remove_file(self, file_path: Path) -> None:
        if file_path.exists():
            file_path.unlink()

    def _is_docker_installed(self) -> None:
        try:
            subprocess.run(["docker", "--version"], capture_output=True, check=True)
        except Exception:
            self.console.print("Warning: Docker is not installed.")

    def _is_pyenv_installed(self) -> None:
        try:
            subprocess.run(["pyenv", "--version"], capture_output=True, check=True)
        except Exception:
            self.console.print("Warning: pyenv is not installed. Please use some python version manager.")

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
                    self.project_directory / ".github" / "workflows" / "draft.yml",
                    self.project_directory / ".github" / "workflows" / "release.yml",
                ],
            ),
        ]

        self._is_pyenv_installed()

        if "{{ cookiecutter.include_docker }}" == "True":
            self._is_docker_installed()

        for condition, paths in conditions_and_paths:
            if condition == "False":
                for path in paths:
                    if path.exists():
                        if path.is_dir():
                            self.console.print(Text(f"Removing folder: {path}", "blue"))
                            self._remove_folder(path)
                        elif path.is_file():
                            self.console.print(Text(f"Removing file: {path}", "blue"))
                            self._remove_file(path)

    def print_further_instructions(self) -> None:
        text_title = Text.assemble("\n", (f"Project: {self.project_slug} was successfully created", "bold blue"))
        text_caption = Text.assemble(("Happy coding! :)", "bold blue"), "\n")

        table = Table(title=text_title, caption=text_caption)

        table.add_column("Task", style="green", no_wrap=True)
        table.add_column("Commands", style="blue")
        table.add_row("GitHub", f"First create a repo that has '{self.project_slug}' as name on Github")
        table.add_row("Connect to repo", "$ make connect_to_repo")
        table.add_row(f"Move in to project: {self.project_slug}", f"$ cd {self.project_slug}")
        table.add_row("Configuring project", "$ make magic")
        table.add_row("Use pre-commit", "$ make pre_commit")

        self.console.print(table)

    def _run_command(self, command: list[str], description: str) -> None:
        text_command = Text(description, "blue")
        self.console.print(text_command)
        subprocess.run(command, check=True)

    def running_pre_installation(self) -> None:
        commands = [(["pip", "install", "--quiet", "--upgrade", "pip", "poetry"], "Upgrading pip, installing poetry")]

        for command, description in commands:
            self._run_command(command, description)

    def modify_pyproject_docs():
        pyproject_path = Path("pyproject.toml")
        if not pyproject_path.exists():
            print("pyproject.toml not found.")
            return

        pyproject_data = toml.load(pyproject_path)

        if "{{ cookiecutter.include_docs_folder }}" == "false":
            pyproject_data.pop("tool.poetry.group.docs.dependencies", None)

        with pyproject_path.open("w") as pyproject_file:
            toml.dump(pyproject_data, pyproject_file)

    def setup(self):
        self.console.print(Text(""))

        with self.console.status("First removing unwanted folders and files..", spinner="dots"):
            self.recursive_removal()

            # with self.console.status("Installing stuff..", spinner="dots"):
            #     self.running_pre_installation()

            self.modify_pyproject_docs()

        self.print_further_instructions()


if __name__ == "__main__":
    project_slug = "{{ cookiecutter.project_slug }}"
    github_user = "{{ cookiecutter.github_username }}"
    setup = PostGenProject(project_slug, github_user)
    setup.setup()
