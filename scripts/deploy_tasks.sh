#!/bin/bash
echo "🔁 Running Django migrations..."
python manage.py migrate --noinput

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput --clear