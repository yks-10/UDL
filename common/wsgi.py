"""
WSGI config for common project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


from django.core.wsgi import get_wsgi_application
from environment.base import set_environment
from environment.variables import EnvironmentVariable

set_environment(EnvironmentVariable.BACKEND_ENVIRONMENT)

application = get_wsgi_application()
