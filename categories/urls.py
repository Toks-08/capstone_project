from rest_framework.routers import DefaultRouter
from django.urls import path, include

from categories.views import CategoryView

router = DefaultRouter()
router.register(r'category', CategoryView)
urlpatterns = router.urls