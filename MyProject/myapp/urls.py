from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home-page' ),
    path('products/', views.viewProducts, name='products-page'),
    path('product/<int:id>/', views.viewOneProduct, name='product-page'),
    path('accounts/', views.viewAccounts, name='accounts-page'),
    path('category/', views.viewCategory, name='category-page'),
    path('add-product/', views.addProduct, name='add-product-page'),

]
