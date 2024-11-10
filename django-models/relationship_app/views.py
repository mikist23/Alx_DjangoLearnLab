from django.shortcuts import render
from django.http import HttpResponse
from relationship_app.models import Book, Library
from django.views.generic import DetailView




# Create your views here.
def list_book(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'list_books.html', context)


class ModelDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_name = 'library'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['book_list'] = library.books.all() 
        return context
