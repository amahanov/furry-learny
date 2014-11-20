__author__ = 'omakhanov'

from rest_framework import serializers
from catalog.models import Author, Book, Genre
from django.shortcuts import get_object_or_404

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title', 'created_dt', 'updated_dt')
        read_only_fields = ('created_dt', 'updated_dt')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class AuthorDatailesSerializer(serializers.ModelSerializer):
    books = serializers.RelatedField(many=True)
    genres = serializers.RelatedField(many=True)

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'genres', 'books')
        read_only_fields = ('created_dt', 'updated_dt')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'pub_year')


class AuthorField(serializers.RelatedField):
    def to_native(self, value):
        return value.__unicode__()

    def from_native(self, value):
        return get_object_or_404(Author, id=value)



class BookDatailesSerializer(serializers.ModelSerializer):
    genre = serializers.RelatedField(many=False, read_only=False)
    author = AuthorField(many=False, read_only=False)
#    author = serializers.RelatedField(many=False, read_only=False)
    class Meta:
        model = Book
        fields = ('id', 'title', 'pub_year', 'publisher_name', 'author', 'genre', 'created_dt', 'updated_dt')
        read_only_fields = ('created_dt', 'updated_dt')

