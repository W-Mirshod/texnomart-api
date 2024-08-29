import django_filters

from product.models import Product, Category


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['lt', 'gt'], }


class CategoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')
    slug = django_filters.CharFilter(lookup_expr='exact', label='Exact Slug')
    custom_field = django_filters.NumberFilter(method='filter_custom_field')

    class Meta:
        model = Category
        fields = ['title', 'slug']

    def filter_custom_field(self, queryset, name, value):
        # Example custom filtering logic
        return queryset.filter(some_related_model__price=value)
