from django.db import models
from django.contrib import admin

class Store(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


admin.site.register(Store)