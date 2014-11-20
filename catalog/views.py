#from django.shortcuts import render
from rest_framework import viewsets

from catalog.models import Genre, Book, Author
from catalog import serializers


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookDetailsViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookDatailesSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorDetailsViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorDatailesSerializer

