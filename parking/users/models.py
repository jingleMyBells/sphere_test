import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uuid = models.UUIDField(
        'uuid',
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(
        'дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'дата изменения',
        auto_now=True,
    )
