from django.shortcuts import render
from .models import Category
from Products.models import Product

# Create your views here.


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'Categories/home.html',
                  {'categories': categories, 'products': products})


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(Category=category)
    return render(request, 'Categories/category_products.html', {'category': category, 'products': products})
