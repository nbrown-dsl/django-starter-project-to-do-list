"""
WSGI config for my_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_app.settings')

application = get_wsgi_application()


#from stack overflow
from my_app.settings import DEBUG
if not DEBUG:    # Running on Heroku
    from dj_static import Cling
    application = Cling(get_wsgi_application())
