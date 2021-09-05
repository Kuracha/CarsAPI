"""Core api urls."""

# 3rd-party
from rest_framework.routers import DefaultRouter

# Local
from .views import CarViewSet
from .views import PopularityViewSet
from .views import RateViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'rate', RateViewSet)
router.register(r'popular', PopularityViewSet, basename='popular')
