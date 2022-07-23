import os

from django.core.asgi import get_sagi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_yamdb.settings')

application = get_asgi_application()
