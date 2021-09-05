"""Core api views."""

# 3rd-party
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# Local
from ..models import Car
from ..models import Rate
from .serializers import CarGetSerializer
from .serializers import CarPostPutDeleteSerializer
from .serializers import PopularitySerializer
from .serializers import RateSerializer


class CarViewSet(viewsets.ModelViewSet):  # noqa: D101
    queryset = Car.objects.all()
    serializer_class = CarPostPutDeleteSerializer
    serializer_class_get = CarGetSerializer
    http_method_names = ['get', 'post', 'delete']

    def retrieve(self, request, *args, **kwargs):  # noqa: D102
        response = {'detail': 'Action retrieve is not allowed'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_serializer_class(self):  # noqa: D102
        if self.action in ['list', 'retrieve']:
            return self.serializer_class_get
        return self.serializer_class


class RateViewSet(viewsets.ModelViewSet):  # noqa: D101
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    http_method_names = ['post']


class PopularityViewSet(viewsets.ModelViewSet):  # noqa: D101
    queryset = Car.objects.all()
    serializer_class = PopularitySerializer
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):  # noqa: D102
        response = {'detail': 'Action retrieve is not allowed'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def list(self, request, *args, **kwargs):  # noqa: D102
        response = super().list(request, *args, **kwargs)
        response.data.sort(key=lambda num: num['rates_number'], reverse=True)
        return response
