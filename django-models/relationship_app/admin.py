from django.contrib import admin
from relationship_app.models import Author, Book, Librarian, Library

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)