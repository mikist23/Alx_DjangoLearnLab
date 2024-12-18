from django.shortcuts import render
from .serializers import  PostSerializer, CommentSerializer, LikeSerializer
from .models import   Post, Comment, Like
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
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification  # Import Notification model
from django.shortcuts import get_object_or_404

# Create your views here.




# __________---------------_______  POST COMMENT VIEWS  ____________ ----------

# -----------_____________USING VIEWSETS___________________---------------------
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


class CommentViewSet(viewsets.ModelViewSet):
    """
        ViewSet for CRUD operations on Comment model.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        """
           Automatically set the author of a comment to the logged-in user.
        """
        serializer.save(author = self.request.user)

    def perform_update(self, serializer):
        """
           Ensure only the author can update the comment.
        """
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied("You do not have permission to edit this comment.")
        serializer.save()
        
    def perform_destroy(self, instance):
        """
           Ensure only the author can delete the comment.
        """
        if instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this comment.")
        instance.delete()

# for user feeds
class UserFeedView(generics.ListAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        # Get the users the current user is following
        following_users = self.request.user.following.all()
        # Retrieve posts from these users, ordered by creation date (most recent first)
        return Post.objects.filter(author__in=following_users).order_by('-created_at')















# -----------_____________USING GENERICS ___________________---------------------
# from rest_framework import generics, permissions
# from rest_framework.exceptions import PermissionDenied
# from .models import Post, Comment
# from .serializers import PostSerializer, CommentSerializer


# # POST Views
# class PostListCreateView(generics.ListCreateAPIView):
#     """
#     List all posts or create a new post.
#     """
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         """
#         Automatically set the author to the logged-in user when creating a post.
#         """
#         serializer.save(author=self.request.user)


# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update, or delete a post.
#     """
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_update(self, serializer):
#         """
#         Ensure only the author can update the post.
#         """
#         post = self.get_object()
#         if post.author != self.request.user:
#             raise PermissionDenied("You do not have permission to edit this post.")
#         serializer.save()

#     def perform_destroy(self, instance):
#         """
#         Ensure only the author can delete the post.
#         """
#         if instance.author != self.request.user:
#             raise PermissionDenied("You do not have permission to delete this post.")
#         instance.delete()


# # COMMENT Views
# class CommentListCreateView(generics.ListCreateAPIView):
#     """
#     List all comments or create a new comment.
#     """
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         """
#         Automatically set the author to the logged-in user when creating a comment.
#         """
#         serializer.save(author=self.request.user)


# class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update, or delete a comment.
#     """
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_update(self, serializer):
#         """
#         Ensure only the author can update the comment.
#         """
#         comment = self.get_object()
#         if comment.author != self.request.user:
#             raise PermissionDenied("You do not have permission to edit this comment.")
#         serializer.save()

#     def perform_destroy(self, instance):
#         """
#         Ensure only the author can delete the comment.
#         """
#         if instance.author != self.request.user:
#             raise PermissionDenied("You do not have permission to delete this comment.")
#         instance.delete()




# +++++++++++____________ LIKES VIEWS SECTION ______+++++++++
# Liking a post view
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            user = request.user

            # Check if the user has already liked the post
            if Like.objects.filter(post=post, user=user).exists():
                return Response({'error': "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Create a like
            # Like.objects.get_or_create(liked_post = post, user_like=user)
            Like.objects.get_or_create(user=request.user, post=post)

            # Create a notification
            content_type = ContentType.objects.get_for_model(Post)
            Notification.objects.create(
                recipient = post.author,
                actor=user,
                verb="Liked",
                content_type=content_type,
                object_id=post.id,

            )

            return Response({"success": "Post liked successfully"}, status=status.HTTP_200_OK)
        

        except Post.DoesNotExist:
            return Response({'error': "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        
# Unliking a post USING APIVIEW

# class UnlikingPostView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#             user = request.user

#             # check if the user have liked the post
#             like = Like.objects.filter(liked_post=post, user_like=user).first()
#             if not like:
#                 return Response({"error": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)

#             # Remove the like
#             like.delete()

#             # Remove the associated notification
#             content_type = ContentType.objects.get_for_model(Post)
#             Notification.objects.filter(
#                 recipient=post.author,
#                 actor=user,
#                 verb="liked",
#                 content_type=content_type,
#                 object_id=post.id,
#             ).delete()

#             return Response({"success": "Post Unliked Successfully"}, status=status.HTTP_200_OK)

#         except Post.DoesNotExist:
#             return Response({'error': "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)


# # Unliking a post USING GENERICAPIVIEW
class UnlikingPostView(generics.GenericAPIView):
    queryset = Post.objects.all()  # Query for the Post model
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            # post = self.get_object()  # Get the Post object using `pk`
            post = generics.get_object_or_404(Post, pk=pk)
            user = request.user

            # Check if the user has liked the post
            like = Like.objects.filter(post=post, user=user).first()
            if not like:
                return Response({"error": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)

            # Remove the like
            like.delete()

            # Remove the associated notification
            content_type = ContentType.objects.get_for_model(Post)
            Notification.objects.filter(
                recipient=post.author,
                actor=user,
                verb="liked",
                content_type=content_type,
                object_id=post.id,
            ).delete()

            return Response({"success": "Post unliked successfully"}, status=status.HTTP_200_OK)

        except Post.DoesNotExist:
            return Response({'error': "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
