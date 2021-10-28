import re
from django.urls import path, include
from rest_framework import routers, generics
from apps.store.views import StoreViewSet, CreateStoreViewSet, ListStoreViewSet


router = routers.DefaultRouter()

router.register(r'store/(?P<name>[^/.]+)', CreateStoreViewSet) #Url create
router.register(r'stores', ListStoreViewSet) #Url list
router.register(r'store', StoreViewSet) #Url get and delete



urlpatterns = [
    path('', include(router.urls)),
]