from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product import serializers
from product.filters import ProductFilter
from product.models import Product, Key, Value
from product.permissions import IsSuperUser


class ProductsPage(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductOnMainPageSerializer
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        page_number = request.GET.get('page', 1)
        cache_key = f'products_page_{page_number}'

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        queryset = self.get_queryset()

        page = paginator.paginate_queryset(queryset, request, view=self)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            paginated_data = paginator.get_paginated_response(serializer.data)

            cache.set(cache_key, paginated_data.data, timeout=600)
            return paginated_data

        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailPage(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProductDeletePage(generics.RetrieveDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProductUpdatePage(generics.RetrieveUpdateAPIView):
    permission_classes = [IsSuperUser]
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
