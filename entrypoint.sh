#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "MySQL started"
fi

# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
# python manage.py loaddata apps/osiete_osint/fixtures/service.json

exec "$@"
