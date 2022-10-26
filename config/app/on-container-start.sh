#!/usr/bin/env bash

# Check for migrations
python manage.py migrate --noinput

# Copy all static files
python manage.py collectstatic --noinput

gunicorn --reload usermng.wsgi:application -b 127.0.0.1:8000 --timeout 60000