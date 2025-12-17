from django.shortcuts import render
from .permissions import IsAdminOrReadOnly

from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets
from .pagination import ProductPagination
# Create your views here
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']
    pagination_class = ProductPagination

