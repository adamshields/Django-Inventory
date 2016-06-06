from django import forms

from .models import Product, Manufacturer, StockStatus

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('item_name', 'item_manufacturer', 'item_stock_status', 'item_active')

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('mfg_name',)

class StockStatusForm(forms.ModelForm):
    class Meta:
        model = StockStatus
        fields = ('stock_stage',)

