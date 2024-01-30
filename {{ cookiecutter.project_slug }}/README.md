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

```sh
pytest
```
