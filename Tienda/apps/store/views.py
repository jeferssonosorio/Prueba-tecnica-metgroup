from rest_framework import status, views
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from apps.store.models import Store
from apps.store.serializers import StoreSerializer


class StoreView(views.APIView):
    """
    A views that provides `get()` `delete()` and `post()` actions.
    """
    def get(self, request, name=None):
        store = get_object_or_404(Store, name=name)
        serializer = StoreSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, name=None):
        store = get_object_or_404(Store, name=name)
        store.delete()
        return Response({"message": "store deleted"})

    def post(self, request, name=None):
        serializer = StoreSerializer(data={"name": name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListStore(views.APIView):
    """
    A view that provides `list()` action.
    """
    def get(self, request):

        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response({"stores": serializer.data}, status=status.HTTP_200_OK)