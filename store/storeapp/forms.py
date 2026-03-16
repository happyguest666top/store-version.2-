from django import forms
from .models import Order_product

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Order_product
        fields = ['amount']