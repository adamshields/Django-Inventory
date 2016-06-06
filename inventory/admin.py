from django.contrib import admin
from .models import Product, Manufacturer, StockStatus

class InventoryAdmin(admin.ModelAdmin):
    list_display = ["item_name", "item_manufacturer", "item_stock_status", "item_active" ]
    class Meta:
        model = Product

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "item_name", "mfg_name", "stock_stage"]

    class Meta:
        model = Manufacturer

class StockStatusAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "item_name", "mfg_name", "stock_stage"]

    class Meta:
        model = StockStatus

admin.site.register(Product, InventoryAdmin)
admin.site.register(Manufacturer)
admin.site.register(StockStatus)

