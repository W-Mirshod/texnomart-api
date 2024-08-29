from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned
from rest_framework import serializers

from product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    images = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_images(self, obj):
        request = self.context["request"]
        try:
            images = obj.images.filter().values_list('image', flat=True)
            absolute_urls = [request.build_absolute_uri(settings.MEDIA_URL + image_path) for image_path in images]
            return absolute_urls
        except obj.images.model.DoesNotExist:
            return None

    def get_ratings(self, obj):
        ratings = obj.ratings.all()
        product_ratings = {}
        for rating in ratings:
            product_ratings['User'] = str(rating.user)
            product_ratings['Product'] = str(rating.product)
            product_ratings['Rating'] = int(rating.value)

        return product_ratings

    def get_is_liked(self, obj):
        likes = obj.is_liked.all()
        product_likes = []
        for like in likes:
            product_likes.append(str(like))

        return product_likes

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryProductsSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    images = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_images(self, obj):
        request = self.context.get('request')
        try:
            try:
                image = obj.images.get(is_primary=True)
                return request.build_absolute_uri(image.image.url)
            except MultipleObjectsReturned:
                image = obj.images.first()
                return request.build_absolute_uri(image.image.url)
        except obj.images.model.DoesNotExist:
            return None

    def get_ratings(self, obj):
        ratings = obj.ratings.all()
        product_ratings = {}
        for rating in ratings:
            product_ratings['User'] = str(rating.user)
            product_ratings['Product'] = str(rating.product)
            product_ratings['Rating'] = int(rating.value)

        return product_ratings

    def get_is_liked(self, obj):
        likes = obj.is_liked.all()
        product_likes = []
        for like in likes:
            product_likes.append(str(like))

        return product_likes

    class Meta:
        model = Product
        fields = '__all__'
