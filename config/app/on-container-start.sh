#!/usr/bin/env bash

# Check for migrations
python manage.py migrate --noinput

# Copy all static files
python manage.py collectstatic --noinput

gunicorn --reload usermng.wsgi:application -b 0.0.0.0:9000 --timeout 60000