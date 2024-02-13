import re
import subprocess
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
MODULE_NAME = "{{ cookiecutter.project_slug }}"
REQUIRED_PYTHON_VERSION = "{{ cookiecutter.python_interpreter }}"


def validate_module_name(name: str) -> bool:
    return re.match(MODULE_REGEX, name) is not None


def check_python_version() -> None:
    try:
        # Get the current Python version using pyenv
        output = subprocess.check_output(["python", "--version"]).decode().strip()
        version_match = re.search(r"\d+\.\d+", output).group()
        if version_match != REQUIRED_PYTHON_VERSION:
            print(
                f"ERROR: Incorrect Python version. Required version is {REQUIRED_PYTHON_VERSION}, but current version is {version_match}."
            )
            print("Please install the required Python version using pyenv and set it as global or local version.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print("ERROR: Could not check Python version using pyenv. Ensure pyenv is installed and set up correctly.")
        print(f"Subprocess output: {e.output.decode().strip()}")
        sys.exit(1)


def main() -> None:
    if not validate_module_name(MODULE_NAME):
        print("ERROR: The project slug '%s' is not a valid Python module name." % MODULE_NAME)
        print("Please use a name that matches the pattern: %s" % MODULE_REGEX)
        sys.exit(1)

    check_python_version()


if __name__ == "__main__":
    main()
