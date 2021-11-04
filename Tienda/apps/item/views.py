from rest_framework import status, views
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from apps.item.models import Item
from apps.item.serializers import ItemSerializer

class ItemView(views.APIView):
    """
    A views that provides `get()` `delete()` `post()` and `put()` actions.
    """
    def get(self, request, name=None):
        item = get_object_or_404(Item, name=name)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, name=None):
        item = get_object_or_404(Item, name=name)
        item.delete()
        return Response({"message": "item deleted"})

    def post(self, request, name=None):
        data = {"name": name}
        data.update(request.data)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name=None):
        item = get_object_or_404(Item, name=name)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListItem(views.APIView):
    """
    A view that provides `list()` action.
    """
    def get(self, request):

        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"items": serializer.data}, status=status.HTTP_200_OK)