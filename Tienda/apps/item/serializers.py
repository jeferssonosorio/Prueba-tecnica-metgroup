from rest_framework import serializers
from apps.item.models import Item

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'store_id']