from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product import serializers
from product.filters import CategoryFilter
from product.models import Category, Product
from product.permissions import IsSuperUser
from product.serializers import CategorySerializer


class CategoriesPage(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter

    def get(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        page_number = request.GET.get("page", 1)
        cache_key = f'categories_page_{page_number}_{request.GET.urlencode()}'

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        queryset = self.filter_queryset(self.get_queryset())
        page = paginator.paginate_queryset(queryset, request)

        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            paginated_data = paginator.get_paginated_response(serializer.data)
            cache.set(cache_key, paginated_data.data, timeout=600)
            return paginated_data

        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryProductsPage(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CategoryProductsSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        category_slug = self.kwargs.get(self.lookup_field)
        category = get_object_or_404(Category, slug=category_slug)
        all_products = Product.objects.filter(category=category)
        return all_products


class CategoryAddPage(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()


class CategoryDeletePage(generics.RetrieveDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = serializers.CategoryDeleteUpdateSerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'


class CategoryUpdatePage(generics.RetrieveUpdateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
