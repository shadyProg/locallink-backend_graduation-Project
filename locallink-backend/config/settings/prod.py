"""Production settings. Run `python manage.py check --deploy` against these."""

from .base import *  # noqa: F401,F403
from .base import env

DEBUG = False

# HTTPS everywhere.
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS: start low and raise it once HTTPS is confirmed working (a long HSTS is hard to undo).
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=3600)
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Only enable behind a reverse proxy you control that sets X-Forwarded-Proto
# and strips it from incoming client requests; otherwise clients can spoof HTTPS.
if env.bool("DJANGO_BEHIND_PROXY", default=False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
