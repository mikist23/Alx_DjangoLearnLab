from django.urls import path
from .views import list_books, LibraryDetailView

from django.views.generic.base import TemplateView
from relationship_app.views import SignUpView

urlpatterns = [
    path('books/', list_books, name = 'list_books'),
     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),



    path('register/',
             TemplateView.as_view(template_name='relationship_app/register.html'),
             name='register'),
    path("signup/", SignUpView.as_view(), name="templates/relationship_app/signup"),
]