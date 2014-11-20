__author__ = 'omakhanov'

from rest_framework import serializers
from catalog.models import Author, Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('title', 'created_dt', 'updated_dt')
        read_only_fields = ('created_dt', 'updated_dt')
