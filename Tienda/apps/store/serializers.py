from rest_framework import serializers
from apps.store.models import Store
from apps.item.serializers import ItemSerializer

class StoreSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'items']


