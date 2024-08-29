from rest_framework import viewsets

from product.models import Product, Category, Attribute
from product.serializers import ProductSerializer, CategorySerializer, AttributeSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
