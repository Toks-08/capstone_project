from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all(),
        allow_null=True
    )
    class Meta:
        model = Category
        fields = ['id','name', 'description', 'created_at', 'parent']
        read_only_fields = ['id', 'created_at']