from rest_framework import viewsets, status, mixins, generics
from rest_framework.response import Response
from apps.store.models import Store
from apps.store.serializers import StoreSerializer


class StoreViewSet(viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    """
    A viewset that provides `retrieve()` and `destroy()` actions.
    """
    queryset = Store.objects.all().order_by('name')
    serializer_class = StoreSerializer
    lookup_field = "name"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"message": "Store deleted"},
                        status=status.HTTP_204_NO_CONTENT)


class ListStoreViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    A viewset that provides `list()` action.
    """
    queryset = Store.objects.all().order_by('name')
    serializer_class = StoreSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response({"stores": serializer.data})


class CreateStoreViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    A viewset that provides `create()` action.
    """
    queryset = Store.objects.all().order_by('name')
    serializer_class = StoreSerializer

    def create(self, request, *args, **kwargs):
        #delete 'store/' from URL
        serializer = self.get_serializer(data={"name": request.path[7:-1]})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


