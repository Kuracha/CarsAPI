"""Core api serializers."""

# Django
from django.db.models import Avg

# 3rd-party
from rest_framework import serializers

# Local
from ..models import Car
from ..models import Rate
from ..validators import check_if_vehicle_exist


class CarPostPutDeleteSerializer(serializers.ModelSerializer):  # noqa: D101

    def validate(self, data):  # noqa: D102
        check_if_vehicle_exist(data)
        return data

    class Meta:  # noqa: D106
        model = Car
        fields = [
            'make',
            'model',
        ]


class CarGetSerializer(serializers.ModelSerializer):  # noqa: D101
    avg_rating = serializers.SerializerMethodField()

    class Meta:  # noqa: D106
        model = Car
        fields = [
            'id',
            'make',
            'model',
            'avg_rating',
        ]

    def get_avg_rating(self, obj):  # noqa: D102
        average_rating = obj.ratings.all().aggregate(Avg('rating'))
        if average_rating['rating__avg']:
            return round(average_rating['rating__avg'], 1)
        return 0.0


class RateSerializer(serializers.ModelSerializer):  # noqa: D101

    class Meta:  # noqa: D106
        model = Rate
        fields = [
            'car_id',
            'rating',
        ]


class PopularitySerializer(serializers.ModelSerializer):  # noqa: D101
    rates_number = serializers.SerializerMethodField()

    class Meta:  # noqa: D106
        model = Car
        fields = [
            'id',
            'make',
            'model',
            'rates_number',
        ]

    def get_rates_number(self, obj):  # noqa: D102
        rates_number = (obj.ratings.all()).count()
        return rates_number
