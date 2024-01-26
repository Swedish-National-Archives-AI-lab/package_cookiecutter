import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{ cookiecutter.project_slug }}"

def validate_module_name(name: str) -> bool:
    return re.match(MODULE_REGEX, name) is not None

def main() -> None:
    if not validate_module_name(module_name):
        print("ERROR: The project slug '%s' is not a valid Python module name." % module_name)
        print("Please use a name that matches the pattern: %s" % MODULE_REGEX)
        sys.exit(1)


if __name__ == "__main__":
    main()
