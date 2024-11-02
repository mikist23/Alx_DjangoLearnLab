<!-- command -->
from bookshelf.models import Book
deleted_book = Book.objects.get(id=1)
deleted_book.delete()
<!-- output -->
Out[23]: (1, {'bookshelf.Book': 1})