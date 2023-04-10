FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONBUFFERED 1

WORKDIR /django

RUN apt-get update \
&& apt-get install -y build-essential \
&& apt-get install -y libpq-dev \
&& apt-get install -y gettext \
&& apt-get install -y netcat gcc postgresql \
&& pip install psycopg2 \
&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

