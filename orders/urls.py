
from .views import OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='orders')

urlpatterns = router.urls