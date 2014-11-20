__author__ = 'omakhanov'

from rest_framework import routers
from catalog import views

router = routers.DefaultRouter()
router.register(r'genre', views.GenreViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'book_detailes', views.BookDetailsViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'author_detailes', views.AuthorDetailsViewSet)

