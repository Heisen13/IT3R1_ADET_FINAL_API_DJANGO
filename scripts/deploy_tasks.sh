#!/bin/bash

echo "🔁 Running Django migrations..."
python manage.py makemigrations attendance
python manage.py migrate --noinput

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput