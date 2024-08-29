from django.contrib import admin

from product.models import Category, Product, Image, Comment, Rating, Key, Value, Attribute


@admin.register(Category)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'updated_at', 'created_at']
    search_fields = ['title', 'slug']
    list_filter = ['title', 'created_at']
    exclude = ['slug']


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


@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['name', 'created_at']


@admin.register(Value)
class KeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['name', 'created_at']


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'product', 'created_at']
    search_fields = ['key', 'product']
    list_filter = ['key', 'product', 'created_at']
