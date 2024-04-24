# DS cookiecutter

[![Sanity checks](https://github.com/Swedish-National-Archives-AI-lab/package_cookiecutter/actions/workflows/test.yml/badge.svg)](https://github.com/Swedish-National-Archives-AI-lab/package_cookiecutter/actions/workflows/test.yml)

A logical, reasonably standardized, but flexible project structure for doing and sharing data science that is package and maintable as software

TLDR;

```bash
python -m cruft create https://github.com/Swedish-National-Archives-AI-lab/package_cookiecutter
```

---

## To get started

Requirements to use the cookiecutter template:

- pyenv
- cookiecutter
- cruft
- toml

## Usage

---

### local-requirements

#### Installing pyenv

**Step 0.**
Open a terminal in the home directory.

```bash
# Ctrl + Alt + T
 cd ~
```

**Step 1.**
To install pyenv on Debian or Ubuntu-based Linux distributions, you have to install several libraries and packages necessary for building Python from scratch. Enter the following command into your terminal to install all necessary packages:

```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
git
```
for ubuntu 22.04 you can follow this guide: https://ericsysmin.com/2024/01/11/how-to-install-pyenv-on-ubuntu-22-04/

**Step 2.**
To install pyenv you can clone it directly from the GitHub repository:

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```


**Step 3.**
After cloning it you need to enter the following commands to add pyenv to your $PATH and start it when a new terminal is opened (if you use a different shell than bash you have to change ~/.bashrc accordingly):

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
```

**Step 3.5**

Restart (repoen) terminal

```bash
exec $SHELL
```

#### Using pyenv

**Step 4.**
After you successfully installed pyenv it is time to look at the different commands that pyenv offers to manage different Python versions.

```bash
pyenv install [PYTHON_VERSION]
```

and to check the version that are installed on your system:

```bash
pyenv versions
```

Now to select a default Python version that is active when you open a new terminal, you use the global command:

**Step 5.**

```bash
pyenv global [PYTHON_VERSION]
```

### Python-requirements

To install python packages:

```bash
pip install cookiecutter cruft
```

### Creating the boilerplate

Set the right python version you want to work with:

```bash
pyenv global [PYTHON_VERSION]
```

Afterwards to get our cookiecutter boilerplate:

```bash
python -m cookiecutter https://github.com/Swedish-National-Archives-AI-lab/package_cookiecutter
```

To have automatically updates and sync cookiecutter boilerplate use cruft:

```bash
python -m cruft create https://github.com/Swedish-National-Archives-AI-lab/package_cookiecutter
```

> Note that poetry is installed and that it creates a venv for the project.

To get the updates from the boilerplate into your project use:

```bash
python -m cruft update
```

---

# For development

## Enviroment

To install Poetry, Cookiecutter, and Cruft on Ubuntu, you can follow these steps. This process involves using the terminal and executing a series of commands.

**Step 1:** Install Poetry
Install Poetry on Ubuntu by running the following command in your terminal:

```bash
pip install poetry
```

**Step 2:** Configure Poetry
Set Virtual Environment Configuration:

```bash
poetry config --local virtualenvs.in-project true
```

**Step 3:** Install Dependencies

```bash
poetry install
```

When you run poetry install, Poetry will install dependencies based on the **poetry.lock** file, ensuring you get the same versions that were used when the lock file was last updated.

- If you need to update the dependencies to their latest versions and update the poetry.lock file accordingly, you can run poetry update instead. This will fetch the latest versions of the dependencies within the constraints specified in pyproject.toml and update the poetry.lock file.

**Step 4:** Activate the Virtual Environment
This activates the virtual environment for your project.

```bash
poetry shell
```

**Step 5:** Install new Dependencies

```bash
poetry add <pipy_package>
```

To install the **pre-commit** package in a group called dev, run the following command:

```bash
poetry add pre-commit --group dev
```

**Step 6:** Exit the Virtual Environment:

```bash
exit
```

## Pre-commit

Pre-commit hooks like ruff and other quality checks to make sure the changeset is in good shape before a commit/push happens.

```bash
pre-commit install
```

```bash
pre-commit run --all-files
```

---

## Ruff

You can configure Ruff to format, fix, and organize imports on-save via the following settings.json:

`ctrl+shift+p`

Install the vscode extension + edit this in setting.json:

```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": true,
      "source.organizeImports": true
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```
