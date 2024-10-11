from django.db import router
from django.urls import path, include
from rest_framework import routers

from .views import VideoViewSet

router = routers.DefaultRouter()

router.register('video', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
