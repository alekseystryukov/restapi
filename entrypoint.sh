#!/bin/sh

while true
do
  python manage.py migrate && break
  sleep 2
done

/usr/local/bin/gunicorn restapi.wsgi --bind 0.0.0.0:8000 --chdir=/app --worker-class=gevent
