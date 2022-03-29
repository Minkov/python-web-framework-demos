from django.urls import path

from drf_demos.api.views import ProductsListView, SingleProductView, CategoriesListView

urlpatterns = (
    # path('products-manual/', ManualProductsListView.as_view(), name='products list'),
    path('products/', ProductsListView.as_view(), name='products list'),
    path('products/<int:pk>/', SingleProductView.as_view(), name='single product'),
    path('categories/', CategoriesListView.as_view(), name='categories list'),
)
