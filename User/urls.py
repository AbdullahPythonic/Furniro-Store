from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name='product_list'),
]