from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.

# author = Author.objects.get(name='Mike')
# books = Book.objects.filter(author=author)
# def  get_author(author_name):
#     author = Author.objects.get(name = author_name)
#     print(f"Book by {author}")

author_name = Author.objects.get(name='Mike')
Author.objects.get(name=author_name)






# List all books in a library.

# books = Library.objects.all()
# Library.objects.get(name='Mike  Absai Library')

books = Book.objects.all()
books.all()







# Retrieve the librarian for a library.

library_name = 'Mike  Absai Library'
library = Library.objects.get(name=library_name)
Librarian.objects.get(library=library)