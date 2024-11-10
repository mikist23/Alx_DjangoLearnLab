from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView




# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    # return render(request, 'list_books.html', context)
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    # template_name = "library_detail.html"
    template_name = "relationship_app/library_detail.html"
    context_name = 'library'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['book_list'] = library.books.all() 
        return context
