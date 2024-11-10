from django.urls import path
from . import views
from relationship_app.views import ModelDetailView

urlpatterns = [
    path('books/', views.list_book, name = 'list_books'),
     path('library/<int:pk>/', ModelDetailView.as_view(), name='library_detail'),
]
