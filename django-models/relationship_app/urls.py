from django.urls import path
from .views import list_books, LibraryDetailView, register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('books/', list_books, name = 'list_books'),
     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

     
     path('login/', auth_views.LoginView.as_view(), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('register/', register, name='register')

    
]