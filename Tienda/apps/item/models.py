from django.db import models
from django.contrib import admin
from apps.store.models import Store


class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits = 5, decimal_places = 2, default=0.00)
    store = models.ForeignKey(Store, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


admin.site.register(Item)
