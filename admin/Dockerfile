FROM python:3.9-alpine

COPY requirements.txt /temp/requirements.txt
COPY admin /admin
WORKDIR /admin
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install --upgrade pip

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password admin-user

USER admin-user