FROM python:3.10.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt update && \
    apt install -y netcat
#    && apt install postgresql-server-dev gcc python3-dev musl-dev
#    && apt install -y gcc python3-dev musl-dev \
#    && apt install -y netcat


WORKDIR /project

COPY source/ .
COPY ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt


#CMD ["/bin/sh", "/project/shell/entrypoint.sh"]