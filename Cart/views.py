from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from Products.models import Product
# from django.contrib.auth.decorators import login_required

# Create your views here.


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.GET.get('quantity', 1))

    cart, created = Cart.objects.get_or_create(product=product, user=request.user)
    if created:
        cart.quantity = quantity
    else:
        cart.quantity += quantity

    cart.save()
    return redirect('cart_detail')


def cart_detail(request):
    cart_item = Cart.objects.filter(user=request.user)
    for item in cart_item:
        item.total_price = item.product.price * item.quantity
    total_price = sum(item.total_price for item in cart_item)
    return render(request, 'Cart/cart_detail.html', {
        'cart_item': cart_item,
        'total_price': total_price,
    })


def delete_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')
