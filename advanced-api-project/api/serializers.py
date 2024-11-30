from .models import Book, Author
from rest_framework import serializers
import datetime
class BookSerializer(serializers.ModelSerializer):
    
    def validate_publication_year(self, value):
        current_year   = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year can not be in the future.")
        return value
    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer) :

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books' ]