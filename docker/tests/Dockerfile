FROM python:3.7-slim

WORKDIR /homework

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pipenv install --deploy --system

COPY app /homework/app
ENTRYPOINT ["/bin/bash", "-c", "cd app && pwd && pytest"]

#ENTRYPOINT ["/bin/sh", "-c" , "<command A> && <command B> && <command C>"]