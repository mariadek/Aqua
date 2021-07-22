#!/bin/bash

echo "$(date): executed script" >> /app/cron.log 2>&1
/usr/local/bin/python /app/src/download.py >> /app/cron.log
