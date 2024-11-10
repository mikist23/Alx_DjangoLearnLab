from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('books/', list_books, name = 'list_books'),
     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

     
     path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
     path('register/', views.register, name='register'),


     path('admin/', views.admin_view, name='admin'),
     path('librarian/', views.librarian_view, name='librarians'),
     path('member/', views.member_view, name='member'),



    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),

    
]