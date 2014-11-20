from django.db import models


class Genre(models.Model):
    title = models.CharField("Genre Title", max_length=50)
    created_dt = models.DateTimeField("Created date and time", auto_now_add=True)
    updated_dt = models.DateTimeField("Updated date and time", auto_now=True)

    class Meta:
        db_table = 'genre'


class Author(models.Model):
    first_name = models.CharField("First name", max_length=50)
    last_name = models.CharField("Last name", max_length=100)
    birth_date = models.DateField("Date of birth")
    created_dt = models.DateTimeField("Created date and time", auto_now_add=True)
    updated_dt = models.DateTimeField("Updated date and time", auto_now=True)
    genres = models.ManyToManyField(Genre, verbose_name="list of authors genres")

    class Meta:
        db_table = 'author'


class Book(models.Model):
    title = models.CharField("Book Title", max_length=500)
    pub_year = models.IntegerField("Publication year")
    publisher_name = models.CharField("Publisher name", max_length=200)
    author = models.ForeignKey(Author, verbose_name="Book Author")
    genre = models.ForeignKey(Genre, verbose_name="Book Genre")
    created_dt = models.DateTimeField("Created date and time", auto_now_add=True)
    updated_dt = models.DateTimeField("Updated date and time", auto_now=True)

    class Meta:
        db_table = 'book'



