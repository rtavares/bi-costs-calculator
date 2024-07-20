FROM python:3.12.4-alpine

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
# RUN #apt update \
#    && apt install postgresql-server-dev gcc python3-dev musl-dev
#    && apt install -y gcc python3-dev musl-dev \
#    && apt install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt