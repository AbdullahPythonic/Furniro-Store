from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    path('contact-me/', TemplateView.as_view
         (template_name="Checkout/Contact-page.html"), name='contact'),
]
