from django.urls import path
from rest_framework.routers import DefaultRouter

from products.views import ProductModelViewSet

router = DefaultRouter()
router.register(r'product', ProductModelViewSet)

urlpatterns = router.urls
