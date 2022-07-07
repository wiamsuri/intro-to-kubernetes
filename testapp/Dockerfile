FROM python:3.10-slim-bullseye

RUN apt-get update

WORKDIR /usr/src/app

ENV POETRY_VERSION 1.1.13
RUN pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock .

RUN poetry install

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
