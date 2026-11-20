from unittest.mock import patch

import pytest
from django.db.utils import OperationalError
from rest_framework.test import APIClient

URL = "/api/v1/health/"


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_health_ok_without_authentication(client):
    response = client.get(URL)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.django_db
def test_health_returns_503_and_hides_details_when_db_down(client):
    db_error = OperationalError("secret db detail")
    with patch("apps.core.views.connection.cursor", side_effect=db_error):
        response = client.get(URL)

    assert response.status_code == 503
    assert response.json() == {"status": "unavailable"}
    assert "secret" not in response.content.decode()


@pytest.mark.django_db
@pytest.mark.parametrize("method", ["post", "put", "patch", "delete"])
def test_health_rejects_non_get_methods(client, method):
    response = getattr(client, method)(URL)

    assert response.status_code == 405
