from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
]
