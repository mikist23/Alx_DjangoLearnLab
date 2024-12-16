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
from rest_framework.exceptions import PermissionDenied

# Create your views here.




# __________---------------_______  POST COMMENT VIEWS  ____________ ----------

class PostViewSet(viewsets.ModelViewSet):
    """
        Viewset for CRUD operations on POst model.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
            Automatically set the author of a post to the logged-in user.
        """
        serializer.save(author = self.request.user)

    def perform_update(self, serializer):
        """
            Ensure only the author can update the post.
        """
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied("You do not have permission to edit this post.")
        serializer.save()
        
    def perform_destroy(self, instance):
        """
           Ensure only the author can delete the post.
        """
        if instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this post.")
        instance.delete()


class CreteCommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]