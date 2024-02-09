from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product


class ProductFilter(FilterSet):
    name = CharFilter(field_name='title', lookup_expr='icontains')
    price_from = NumberFilter(field_name='price', lookup_expr='gte')
    price_to = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = []