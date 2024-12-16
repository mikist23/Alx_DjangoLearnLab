from django.shortcuts import render
from .serializers import RegistrationSerializer, PostSerializer, CommentSerializer, ListUsersSerializer, TokenSerializer, DeleteUserSerializer, UserProfileSerializer
from .models import CustomUser, Post, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets

# Create your views here.




# __________---------------_______  POST COMMENT VIEWS  ____________ ----------

class CretePostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class CreteCommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]