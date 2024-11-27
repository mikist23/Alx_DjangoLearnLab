from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializers
from .models import Book

# Create your views here.

class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers