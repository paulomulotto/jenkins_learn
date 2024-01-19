FROM python:3.11-buster

RUN pip install poetry==1.7.1

WORKDIR /app

COPY pyproject.toml pytest.ini poetry.lock ./
COPY tests ./tests

RUN poetry install

COPY python_pipeline_jenkins_learn ./python_pipeline_jenkins_learn

WORKDIR /app/python_pipeline_jenkins_learn