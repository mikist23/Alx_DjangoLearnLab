from django.urls import path
from .views import Booklist

urlpatterns = [
    path('books/', Booklist.as_view(), name = "book-list")
]