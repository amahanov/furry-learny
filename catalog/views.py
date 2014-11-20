#from django.shortcuts import render
from rest_framework import viewsets

from catalog.models import Genre
from catalog.serializers import GenreSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

#    class Meta:
#        model = Genre

