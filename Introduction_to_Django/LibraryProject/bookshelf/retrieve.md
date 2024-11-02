<!-- command -->
retrived_book = Book.objects.get(title='1984')
retrived_book.title = "Nineteen Eighty-Four"

<!-- output -->
retrived_book.author
Out[15]: 'George Orwell'