import logging

from django.db import connection, transaction
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

logger = logging.getLogger(__name__)


# non_atomic_requests must be the OUTERMOST decorator. With ATOMIC_REQUESTS on, Django opens a
# transaction before the view runs; if the DB is down that fails outside our try/except and
# the monitor would see a 500 instead of the intended 503.
@transaction.non_atomic_requests
@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    """Liveness + database reachability. Public on purpose: monitors call it."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except Exception:
        # Log the detail server-side; never leak DB errors to the caller.
        logger.exception("Health check: database unreachable")
        return Response({"status": "unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    return Response({"status": "ok"})
