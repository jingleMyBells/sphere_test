import uuid

from django.db import models


class Vehicle(models.Model):
    uuid = models.UUIDField(
        'uuid',
        default=uuid.uuid4,
        editable=False,
    )
    brand = models.CharField(
        verbose_name='марка авто',
        max_length=100,
    )
    model = models.CharField(
        verbose_name='модель авто',
        max_length=100,
    )
    plate_number = models.CharField(
        verbose_name='номер авто',
        max_length=10,
    )
    owners_name = models.CharField(
        verbose_name='ФИО владельца',
        max_length=100,
    )
    created_at = models.DateTimeField(
        'дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'дата изменения',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'

    def __str__(self):
        return self.brand + ' ' + self.model + ' ' + self.plate_number
