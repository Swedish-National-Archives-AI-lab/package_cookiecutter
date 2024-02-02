FROM python:{{cookiecutter.python_interpreter}}

WORKDIR /usr/src/app

RUN pip install poetry

COPY . .

RUN poetry install

CMD [ "poetry", "run", "./src/{{cookiecutter.package_name}}/main.py"]

# Commands:
# Build a docker image:
# docker build -t [tag] [dockerfile position] e.g docker build -t python_hello_world .  (. since docker is in the same folder)
# Check your images:
# docker images                (e.g you should see: python_hello_world)

# Create and run a Docker container
# docker run [docker image]  e.g docker run python_hello_world

# How to get into a docker container
# docker run -it [docker image] /bin/bash

# to exit docker
# use command: exit

# docker ps -all
# docker kill <name>