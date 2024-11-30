from django.urls import path
from .views import (
    CustomBookCreateView,
    CustomBookDeleteView,
    CustomBookDetailView,
    CustomBookListView,
    CustomBookUpdateView)

urlpatterns = [

    path('books/', CustomBookListView.as_view(), name='list_books'),
    path('books/<int:id>/', CustomBookDetailView.as_view(), name='detail_books'),
    path('books/create/', CustomBookCreateView.as_view(), name='create_books'),
    path('books/<int:id>/update/', CustomBookUpdateView.as_view(), name='update_books'),
    path('books/<int:id>/delete/', CustomBookDeleteView.as_view(), name='delete_books'),
]