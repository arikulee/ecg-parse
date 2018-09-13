FROM python:3.7-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    build-essential \
    && apt-get install -y tk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app
