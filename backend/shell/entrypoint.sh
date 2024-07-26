#!/bin/sh

 echo "Connection Data:" $POSTGRES_HOST $POSTGRES_PORT
# DJANGO_SETTINGS_MODULE defined in .env / docker-compose.yaml environment
echo "DJANGO_SETTINGS_MODULE: ${DJANGO_SETTINGS_MODULE}"

if [ "$DJANGO_DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    echo "Data:" $POSTGRES_HOST $POSTGRES_PORT

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.6
    done

    echo "PostgreSQL started"
fi

/project/products_prices/manage.py migrate
/project/products_prices/manage.py collectstatic --no-input


# Prod
# gunicorn --chdir products_prices products_prices.wsgi:application  --bind 0.0.0.0:$DJANGO_INTERNAL_PORT
# Dev
#gunicorn --chdir products_prices products_prices.wsgi:application  --bind 0.0.0.0:$DJANGO_INTERNAL_PORT --reload
cd /project/products_prices
/project/products_prices/manage.py runserver 0.0.0.0:$DJANGO_INTERNAL_PORT

exec "$@"
