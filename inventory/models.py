from django.db import models
from django.core.urlresolvers import reverse

# Products
class Product(models.Model):
    item_name = models.CharField(max_length=300, verbose_name="Product")
    item_location = models.CharField(max_length=300, verbose_name="Location", null=True, blank=True)
    item_active = models.BooleanField(default=False,verbose_name="Active")
    item_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, verbose_name="Manufacturer", null=True, blank=True)
    item_stock_status = models.ForeignKey('StockStatus', on_delete=models.CASCADE, verbose_name="Stock Status", null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("inventory_detail", kwargs={"slug": self.slug})

# Stock Status
class StockStatus(models.Model):
    """
    Stock status values such as "In Stock", "Backordered", etc.
    """
    stock_stage = models.CharField(max_length=50)

    class Meta():
        verbose_name_plural = 'Stock Status'

    def __str__(self):
        return self.stock_stage

class Manufacturer(models.Model):
    mfg_name = models.CharField(max_length=300, blank=True, verbose_name="Manufacturer")

    def __str__(self):
        return self.mfg_name

class Recipes(models.Model):
    flavor_name = models.CharField(max_length=300, verbose_name="Item")

    item_stock_status = models.ForeignKey('StockStatus', on_delete=models.CASCADE, verbose_name="Stock Status")

    def __str__(self):
        return self.item_name