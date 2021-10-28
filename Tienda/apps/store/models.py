from django.db import models
from django.contrib import admin

class Store(models.Model):
    #Es único por que es el lookup usado en los endpoints
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


admin.site.register(Store)