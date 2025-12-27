from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets
from .pagination import ProductPagination
from rest_framework.decorators import action
# Create your views here
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']
    pagination_class = ProductPagination

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
        queryset = self.get_queryset()

        search = request.query_params.get("search")
        category = request.query_params.get("category")

        if search:
            queryset = queryset.filter(name__icontains=search)

        if category:
            queryset = queryset.filter(category__name__icontains=category)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)