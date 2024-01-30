# {{ cookiecutter.project_name }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug}}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![Built with Riksarkivet DS cookiecutter](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/Swedish-National-Archives-AI-lab/package_cookiecutter)

---

{%- if cookiecutter.include_docs_folder == "y" -%}
**Documentation**: [https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug}}](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug}})
{% endif %}
**Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

**PyPI**: [https://pypi.org/project/{{ cookiecutter.project_slug }}/](https://pypi.org/project/{{ cookiecutter.project_slug }}/)

---

{{ cookiecutter.project_short_description }}

## Installation

```sh
pip install {{ cookiecutter.project_slug }}
```

## Development

- Clone this repository
- Requirements:
  - [Poetry](https://python-poetry.org/)
  - Python {{ cookiecutter.python_interpreter }}+
- Create a virtual environment and install the dependencies

```sh
poetry install
```

- Activate the virtual environment

```sh
poetry shell
```

### Testing

Poetry provides a run command to execute the given command inside the project’s virtual environment. So execute the following command to run the tests:

```sh
poetry run pytest -v
```

And if your inside the virtual environment run:

```sh
pytest
```

### Building the package

For Poetry, the equivalent of `pip install -e` . (which is used to install a package in editable mode with pip) is to use the poetry install command in the root directory of the project.

When you run `poetry install` in a project that is managed by Poetry, it installs the project's dependencies as well as the project itself in editable mode. This means that changes to the project's code will immediately affect the installed package without the need for reinstallation.

> You can run poetry install whether you're inside the Poetry-created virtual environment (activated using poetry shell) or not. Poetry will handle the installation of the project in editable mode correctly in either case.

### Publish the Package

But before you can publish your library, you need to package it with the build command:

```sh
poetry build
```

To publish your library, you will need to properly configure your PyPI credentials, as Poetry will publish the library to PyPI by default.

```sh
poetry config repositories.test-pypi https://test.pypi.org/legacy/
```

Configure key:

```sh
poetry config pypi-token.test-pypi pypi-<tokenv_value>
```

Once the library is packaged, you can use the publish command to publish it.

```sh
# Only `poetry publish` will push by default to pypi directly
poetry publish -r test-pypi
```
