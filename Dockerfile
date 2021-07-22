# syntax=docker/dockerfile:1

FROM python:3.6

RUN apt-get update && apt-get -y install cron

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

COPY /src /app/src

COPY crontab /etc/cron.d/crontab

COPY script.sh /app/script.sh

RUN chmod 0644 /etc/cron.d/crontab

RUN /usr/bin/crontab /etc/cron.d/crontab

CMD ["cron", "-f"]
