FROM python:3.10-alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /temp/requirements.txt
COPY landing /landing
WORKDIR /landing
EXPOSE 8000

RUN pip install -r /temp/requirements.txt
