"""Local development settings. Never use in production."""
import environ
import os

from .base import *  # noqa: F401,F403

DEBUG = True
# 10.0.2.2 is how the Android emulator reaches the host machine.
#ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
