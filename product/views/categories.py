from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product import serializers
from product.models import Category, Product


class CategoriesPage(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        cache_key = f'categories_page_{request.GET.get("page", 1)}'
        category_data = cache.get(cache_key)

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(category_data, status=status.HTTP_200_OK)
        categories = Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True, context={'request': request})
        category_data = serializer.data
        cache.set(cache_key, category_data, timeout=600)

        return Response(category_data, status=status.HTTP_200_OK)


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
    permission_classes = [AllowAny]
    serializer_class = serializers.CategoryDeleteUpdateSerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'


class CategoryUpdatePage(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
