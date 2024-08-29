from django.urls import path

from product import views

urlpatterns = [
    # categories
    path('categories/', views.CategoriesPage.as_view()),
    path('category/add-category/', views.CategoryAddPage.as_view()),
    path('category/<slug:slug>/', views.CategoryProductsPage.as_view()),
    path('category/<slug:slug>/delete', views.CategoryDeletePage.as_view()),
    path('category/<slug:slug>/edit', views.CategoryUpdatePage.as_view()),

    # products
    path('', views.ProductsPage.as_view()),
]
