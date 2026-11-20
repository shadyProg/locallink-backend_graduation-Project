import uuid

from django.db import models


class BaseModel(models.Model):
    """Abstract base for every domain model: UUID primary key + audit timestamps.

    UUID keys make IDs non-guessable (no /resource/5 enumeration). This is
    defense in depth only: every endpoint must still check ownership.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
