from rest_framework import serializers
from .models import Product
from categories.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    category_name = serializers.SlugRelatedField(
        source='category',  # points to the ForeignKey
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'price', 'is_active', 'created_at', 'description',
                  'updated_at', 'category', 'category_name']
        read_only_fields = ['id', 'slug', 'is_active', 'created_at',
                  'updated_at', 'category_name']

        def create(self, validated_data):
            # Remove category from validated_data and pass it explicitly
            category = validated_data.pop('category')
            product = Product.objects.create(**validated_data, category=category)
            return product