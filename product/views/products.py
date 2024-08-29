from rest_framework import generics
from rest_framework.permissions import AllowAny

from product import serializers
from product.models import Product, Key, Value


class ProductsPage(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductOnMainPageSerializer
    queryset = Product.objects.all()


class ProductDetailPage(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProductDeletePage(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProductUpdatePage(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class KeyPage(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.KeySerializer
    queryset = Key.objects.all()


class ValuePage(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ValueSerializer
    queryset = Value.objects.all()
