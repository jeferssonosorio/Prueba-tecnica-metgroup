from django.urls import path
from apps.item.views import ItemView, ListItem

urlpatterns = [
    path('items', ListItem.as_view()),
    path('item/<str:name>/', ItemView.as_view()),
]