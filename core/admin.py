"""Core admin."""

# Django
from django.contrib import admin

# Local
from .models import Car
from .models import Rate


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):  # noqa: D101

    fields = [
        'make',
        'model',
    ]

    list_display = [
        'make',
        'model',
    ]


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):  # noqa: D101
    fields = [
        'car_id',
        'rating',
    ]

    list_display = [
        'car_id',
        'rating',
    ]
