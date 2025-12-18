from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
# Create your views here.

class CartView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return carts belonging to the logged-in user
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user to the logged-in user
        serializer.save(user=self.request.user)

class CartItemView(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return CartItems belonging to the user's active cart
        user_cart = Cart.objects.filter(user=self.request.user, is_active=True).first()
        if user_cart:
            return CartItem.objects.filter(cart=user_cart)
        return CartItem.objects.none()

    def perform_create(self, serializer):
        # Add item to the user's active cart
        user_cart, created = Cart.objects.get_or_create(user=self.request.user, is_active=True)

        # If the product already exists in the cart, increase quantity
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()