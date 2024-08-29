from django.core.cache import cache
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product import serializers
from product.models import Product, Key, Value


class ProductsPage(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductOnMainPageSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        cache_key = f'products_page_{request.GET.get("page", 1)}'
        product_data = cache.get(cache_key)

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(product_data, status=status.HTTP_200_OK)
        products = Product.objects.all()
        serializer = serializers.ProductOnMainPageSerializer(products, many=True, context={'request': request})
        product_data = serializer.data
        cache.set(cache_key, product_data, timeout=600)

        return Response(product_data, status=status.HTTP_200_OK)


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
