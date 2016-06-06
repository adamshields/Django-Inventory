# inventory

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class StockStatus(models.Model):
    """
    Stock status values such as "In Stock", "Backordered", etc.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta():
        verbose_name_plural = 'Stock Status'

    def __unicode__(self):
        return self.name


class InventoryItem(models.Model):
    """
    An inventoried item represented by any Django model by means of the Content
    Types framework.
    """
    sku = models.CharField(max_length=75, unique=True, db_index=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=50, blank=True, null=True)
    stock_status = models.ForeignKey(StockStatus, db_index=True)
    stock_comment = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        content_type = ContentType.objects.get_for_model(self.content_object)
        return str(content_type.get_object_for_this_type(pk=self.object_id))


class Transaction(models.Model):
    """
    A transaction which adds or removes items from inventory.
    """