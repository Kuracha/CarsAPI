"""Core models."""

# Django
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


class Car(models.Model):  # noqa: D101
    make = models.CharField('Make', max_length=64)
    model = models.CharField('Model', max_length=64, unique=True)

    class Meta:  # noqa: D106
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):  # noqa: D105
        return str(self.id)


class Rate(models.Model):  # noqa: D101
    car_id = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Car',
        related_name='ratings',
    )
    rating = models.PositiveIntegerField(
        'Rating',
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    class Meta:  # noqa: D106
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

    def __str__(self):  # noqa: D105
        return f'{self.car_id} {self.rating}'
