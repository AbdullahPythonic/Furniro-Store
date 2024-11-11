from django.shortcuts import render, redirect
from .models import Checkout
from Cart.models import Cart
from .forms import OrderForm
# Create your views here.


def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity
                      for item in cart_items)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.save()
            order.cart.set(cart_items)

            for item in cart_items:
                item.product.stock -= item.quantity
                item.product.save()

            cart_items.delete()

            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'Checkout/order.html', {
        'form': form,
        'cart_items': cart_items,
        'total_price': total_price,
    })


def order_success(request):
    order = Checkout.objects.filter(user=request.user).order_by('-created_on').first()
    if not order:
        return redirect('all_products')

    total_price = order.total_price

    return render(request, 'Checkout/order-success.html', {
        'total_price': total_price
    })
