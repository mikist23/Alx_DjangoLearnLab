from django.urls import path
from .views import (
    CustomBookCreateView,
    CustomBookDeleteView,
    CustomBookDetailView,
    CustomBookListView,
    CustomBookUpdateView)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    

    path('books/', CustomBookListView.as_view(), name='list_books'),
    path('books/<int:id>/', CustomBookDetailView.as_view(), name='detail_books'),
    path('books/create/', CustomBookCreateView.as_view(), name='create_books'),
    # path('books/<int:id>/update/', CustomBookUpdateView.as_view(), name='update_books'),
    # path('books/<int:id>/delete/', CustomBookDeleteView.as_view(), name='delete_books'),
    path('books/update', CustomBookUpdateView.as_view(), name='update_books'),
    path('books/delete', CustomBookDeleteView.as_view(), name='delete_books'),
    path('token/', obtain_auth_token, name = 'api_token' ),
]