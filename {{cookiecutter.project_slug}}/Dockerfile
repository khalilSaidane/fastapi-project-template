FROM python:3.7.9-buster

ENV PYTHONUNBUFFERED 1

# https://python-poetry.org/docs/#installation
ARG POETRY_VERSION=1.1.2
ARG POETRY_HOME=/usr/local/poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV PYTHONPATH $PYTHONPATH:$POETRY_HOME/lib

WORKDIR /app
COPY pyproject.toml poetry.lock ./

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.in-project true \
    && poetry config virtualenvs.path /app/venv \
    && poetry install

COPY . /app

EXPOSE 8000
CMD cd {{cookiecutter.project_slug}} && poetry run uvicorn --host=0.0.0.0 main:app
