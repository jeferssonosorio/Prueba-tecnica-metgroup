from django.urls import path, include
from rest_framework import routers
from apps.store.views import StoreViewSet


router = routers.DefaultRouter()
router.register('mi_tienda', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]