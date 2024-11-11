from django import forms
from .models import Checkout


class OrderForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['first_name', 'last_name', 'country', 'city', 'address',
                  'postal_code', 'phone', 'email']
