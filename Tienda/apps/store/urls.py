import re
from django.urls import path, include
from apps.store.views import StoreView, ListStore



urlpatterns = [
    path('stores', ListStore.as_view()),
    path('store/<str:name>/', StoreView.as_view()),
]