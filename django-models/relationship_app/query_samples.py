from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
author = Author.objects.get(name='Mike')
books = Book.objects.filter(author=author)

# List all books in a library.
# books = Library.objects.all()
# Library.objects.get(name='Mike  Absai Library')
library_name = 'Mike  Absai Library'
Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library.
