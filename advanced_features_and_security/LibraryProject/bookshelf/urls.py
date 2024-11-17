from django.urls import path
from bookshelf.views import book_list

urlpatterns = [
    path('books', book_list, name='books' )
]