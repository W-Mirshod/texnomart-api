from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from product.models import Category, Product, Image, Comment, Rating, Key, Value, Attribute


class ProductsResource(resources.ModelResource):
    class Meta:
        model = Product
        exclude = ()


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        exclude = ()


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'slug', 'updated_at', 'created_at']
    search_fields = ['title', 'slug']
    list_filter = ['title', 'created_at']
    exclude = ['slug']
    resource_class = CategoryResource


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'created_at']
    search_fields = ['name', 'slug']
    list_filter = ['name', 'price', 'created_at']
    exclude = ['slug']
    resource_class = ProductsResource


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
