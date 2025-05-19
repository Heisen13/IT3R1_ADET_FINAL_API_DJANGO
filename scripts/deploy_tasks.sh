#!/bin/bash

# Migrate the database
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput
