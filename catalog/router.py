__author__ = 'omakhanov'

from django.conf.urls import url, include
from rest_framework import routers
from catalog import views

router = routers.DefaultRouter()
router.register(r'genres', views.UserViewSet)

