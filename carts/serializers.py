from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()
    class Meta:
        model = CartItem
        fields = ['id', 'subtotal', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cart_items', many=True, read_only=True)
    total = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['user', 'created_at', 'updated_at','id']

        def get_total(self, obj):
            # Sum up subtotal of all cart items
            return sum(item.subtotal for item in obj.cart_items.all())
