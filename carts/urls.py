from rest_framework.routers import DefaultRouter
from .views import CartView, CartItemView

router = DefaultRouter()
router.register(r'cart', CartView, basename='cart')
router.register(r'cart-items', CartItemView, basename='cart-item')

urlpatterns = router.urls
