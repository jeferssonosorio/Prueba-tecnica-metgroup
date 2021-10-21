from rest_framework import viewsets, status, generics, mixins
from apps.store.models import Store
from apps.store.serializers import StoreSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
