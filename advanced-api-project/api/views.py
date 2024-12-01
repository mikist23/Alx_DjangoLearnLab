from django.shortcuts import render
from .models import Book, Author
from rest_framework import generics, permissions, status, authentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework

# Create your views here.

class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']

    # searching
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

    # ordering
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']

class CustomBookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class CustomBookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    

    def perorm_create(self, serializer):
        if not serializer.valiated_data.get('publication_year'):
            serializer.validated_data['publication_year'] = 2024
        serializer.save()

class CustomBookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    lookup_field = 'id'

class CustomBookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'