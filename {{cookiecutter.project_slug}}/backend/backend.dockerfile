FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y

COPY . /app/
COPY requrements.txt /app/confs/requrements.txt

RUN pip install -r /app/confs/requrements.txt
