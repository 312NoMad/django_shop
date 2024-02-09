from rest_framework import serializers

from .models import Product, Category, Tag, Review


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all(), required=False)

    class Meta:
        fields = '__all__'
        model = Product


class CategorySerializer(serializers.ModelSerializer):
    # products = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all(), many=True)
    products = serializers.IntegerField(source='products.count', read_only=True)

    class Meta:
        fields = ('id', 'name', 'description', 'products', 'tags')
        model = Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product', 'text', 'rating')
