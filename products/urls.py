from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet

router = DefaultRouter()
router.register(r'product', ProductModelViewSet)


urlpatterns = router.urls
