from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CategorySerializer
from .models import Category
from rest_framework import viewsets
# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

