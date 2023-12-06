# DS cookiecutter

A logical, reasonably standardized, but flexible project structure for doing and sharing data science that is package and maintable as software

## To get started

Requirements to use the cookiecutter template:

- Python 3.7+
- Cookiecutter Python package >= 1.4.0: This can be installed with pip or conda.

To install cookiecutter:

`$ pip install cookiecutter`

To get cookiecutter:

`$ python -m cookiecutter https://github.com/Borg93/ds_cookiecutter
`

## Project Structure

---

    ├── LICENSE
    ├── Makefile             <- Makefile with commands. Start with `make help`
    │
    ├── data
    │   ├── external         <- Data from third party sources.
    │   ├── interim          <- Intermediate data that has been transformed.
    │   ├── processed        <- The final, canonical data sets for modeling.
    │   └── raw              <- The original, immutable data dump.
    │
    ├── docs                 <- A default wiki folder that should be hosted in Azure devops Wiki
    │   └── README           <- Long description of project
    │
    ├── models               <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks            <- Jupyter notebooks. (your debug folder)
    │
    ├── tests                <- Put all your tests here.
    │   ├── unit
    │   └── integration
    │
    ├── MANIFEST             <- Files that should be included in build
    │
    ├── .gitignore           <- "What not to push"
    ├── .env                 <- SHOULD NOT BE PUSHED! store token/key/secrets for local dev here.
    │
    ├── .pre-commit-config   <- To check commits before commiting to main
    ├── .github              <- github CI/CD pipeline recipe
    ├──  mkdocs.yml          <- mkdocs recipe
    │
    ├── requirements.txt     <- The requirements file for reproducing the analysis environment, e.g.
    │                           generated with `pip freeze > requirements.txt`
    ├── requirements_dev.txt <- The dev requirements file for building and testing
    │
    ├── setup.py             <- makes project pip installable (pip install -e .) so src can be imported + metadata for build
    ├── pyproject.toml       <- toml file to control configs of other packages (such as flake8.ini) 
    │
    ├── src                  <- Source code for use in this project.
    │   └── package_name
    │       ├── __init__.py  <- Makes src a Python module
    │       │
    │       └── main         <- Temporary Script..
    │
    └── tox.ini              <- tox file with settings for running tox; see tox.readthedocs.io

---

## Trunk at Scale

This cookiecutter supports the development style Trunk-Based Development (TBD) to enable DS-package which can be reused between projects.
