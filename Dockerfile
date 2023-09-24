FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock  requerements.txt /code/

RUN pip install pipenv && pipenv install --system

RUN pip install -r requerements.txt

COPY . /code/