from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'country', 'state', 'city', 'postal_code', 'house_number', 'building_name','address_line_1', 'address_line_2', 'order_note']