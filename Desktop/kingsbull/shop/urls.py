from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('shopping/', views.shopping_page, name='shopping_page'),
    path('create-checkout-session/<int:amount>/', views.create_checkout_session, name='create_checkout_session'),
]
