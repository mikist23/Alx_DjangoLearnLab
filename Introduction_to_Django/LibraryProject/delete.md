<!-- command -->
In [22]: retrived_book = Book.objects.get(id=2)
<!-- output -->
In [23]: retrived_book.delete()
Out[23]: (1, {'bookshelf.Book': 1})