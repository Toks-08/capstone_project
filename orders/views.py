from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from carts.models import Cart, CartItem
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.db import transaction


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # only users can see their own orders
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    @transaction.atomic
    def checkout(self, request):
        user = request.user
        #get active cart and cart item
        cart = Cart.objects.filter(user=user, is_active=True).first()
        if not cart:
            return Response({
                'details':'no active cart found'
            }, status=status.HTTP_400_BAD_REQUEST)
        cart_item = CartItem.objects.filter(cart=cart)
        if not cart_item.exists():
            return Response({
                'details': 'Cart is Empty'
            }, status=status.HTTP_400_BAD_REQUEST)

        #creating an order
        user = request.user
        order = Order.objects.create(
            user=user,
            total_amount = 0,
            status = 'PENDING',
            payment_status = 'UNPAID'
        )
        total = 0

        #Create order item
        for item in cart_item:
            OrderItem.objects.create(
                order=order,
                product= item.product,
                price_at_purchase = item.product.price,
                quantity = item.quantity
            )
            total += item.product.price * item.quantity

        #finalize order
        order.total_amount = total
        order.save()

        #close cart
        cart.is_active = False
        cart.save()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

