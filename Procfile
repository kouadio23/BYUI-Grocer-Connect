web: bash run-daphne.sh
channel_worker: python manage.py runworker channel_layer -v2
release: python manage.py migrate
gunicorn byuiGrocerConnect.wsgi:application --timeout 60