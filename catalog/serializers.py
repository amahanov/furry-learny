__author__ = 'omakhanov'

from rest_framework import serializers
from catalog.models import Author, Book, Genre


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


class BookDatailesSerializer(serializers.ModelSerializer):
    genre = serializers.RelatedField(many=False)
    author = serializers.RelatedField(many=False)
    class Meta:
        model = Book
        fields = ('id', 'title', 'pub_year', 'publisher_name', 'author', 'genre', 'created_dt', 'updated_dt')
        read_only_fields = ('created_dt', 'updated_dt')

