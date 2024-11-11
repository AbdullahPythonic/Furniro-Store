from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('delete/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
]
