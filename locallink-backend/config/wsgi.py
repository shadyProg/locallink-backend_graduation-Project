import os

from django.core.wsgi import get_wsgi_application

# Default to the SAFE settings; dev must opt in via manage.py or the environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

application = get_wsgi_application()
