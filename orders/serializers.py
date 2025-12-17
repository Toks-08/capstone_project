from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price_at_purchase']
        read_only_fields = ['id', 'product', 'quantity', 'price_at_purchase', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='order_items', many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id','status', 'payment_status', 'total_amount', 'created_at', 'updated_at']
        read_only_fields = ['id','status', 'payment_status', 'total_amount', 'created_at', 'updated_at', 'items']
