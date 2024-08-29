from django.urls import path

from product.views import products, categories

urlpatterns = [
    # categories
    path('categories/', categories.CategoriesPage.as_view()),
    path('category/add-category/', categories.CategoryAddPage.as_view()),
    path('category/<slug:slug>/', categories.CategoryProductsPage.as_view()),
    path('category/<slug:slug>/edit', categories.CategoryUpdatePage.as_view()),
    path('category/<slug:slug>/delete', categories.CategoryDeletePage.as_view()),

    # products
    path('', products.ProductsPage.as_view()),
    path('product/detail/<slug:slug>/', products.ProductDetailPage.as_view()),
    path('product/detail/<slug:slug>/edit/', products.ProductUpdatePage.as_view()),
    path('product/detail/<slug:slug>/delete/', products.ProductDeletePage.as_view()),

    # attributes
    path('attribute-key/', products.KeyPage.as_view()),
    path('attribute-value/', products.ValuePage.as_view()),
]
