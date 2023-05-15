release: python manage.py migrate --no-input --settings=stock_service.settings.prod
web gunicorn stock_service.wsgi --log-file -
