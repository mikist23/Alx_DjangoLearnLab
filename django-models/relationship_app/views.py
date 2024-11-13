from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library, UserProfile
from django.views.generic.detail import DetailView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test





from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Book 
from django.contrib.auth.decorators import permission_required



# Create your views here.
def list_books(request):
    books = Book.objects.all()
    # context = {'book_list': books}
    # return render(request, 'list_books.html', context)
    return render(request, 'relationship_app/list_books.html', {'book_list': books})


class LibraryDetailView(DetailView):
    model = Library
    # template_name = "library_detail.html"
    template_name = "relationship_app/library_detail.html"
    context_name = 'library'  
    
@login_required
def home(request):
    return render(request, 'relationship_app/home.html')


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
    return user.userprofile.role == 'Librarian'

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













@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Add logic to create a book entry
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to edit a book
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to delete a book
    return redirect('list_books')