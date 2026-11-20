from django.contrib import admin
from django.urls import include, path

from config.settings.base import ADMIN_URL  # noqa: F401  (shared across all environments)

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path("api/v1/", include("apps.core.urls")),
]
