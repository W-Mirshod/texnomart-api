from django.contrib import admin

from product.models import Category, Product, Image, Comment, Rating


@admin.register(Category)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'updated_at', 'created_at']
    search_fields = ['title', 'slug']
    list_filter = ['title', 'created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'created_at']
    search_fields = ['name', 'slug']
    list_filter = ['name', 'price', 'created_at']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'is_primary', 'created_at']
    list_filter = ['product', 'created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_published', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['product', 'created_at']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'value', 'created_at']
    search_fields = ['user', 'product']
    list_filter = ['user', 'product', 'created_at']
