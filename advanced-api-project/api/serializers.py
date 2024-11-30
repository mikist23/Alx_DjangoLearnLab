from .models import Book, Author
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer) :

    name = BookSerializer(many = True, read_only = True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'title', 'publication_year', 'author' ]