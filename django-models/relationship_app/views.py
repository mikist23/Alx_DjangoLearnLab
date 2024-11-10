from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test



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


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form':form})








def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarians'

def is_member(user):
    return user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')