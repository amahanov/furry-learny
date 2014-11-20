__author__ = 'omakhanov'

from rest_framework import routers
from catalog import views

router = routers.DefaultRouter()
router.register(r'genre', views.GenreViewSet)
router.register(r'book', views.BookViewSet, base_name='book')
router.register(r'book_detailes', views.BookDetailsViewSet, base_name='book_datailes')
router.register(r'author', views.AuthorViewSet, base_name='author')
router.register(r'author_detailes', views.AuthorDetailsViewSet, base_name='author_detailes')

