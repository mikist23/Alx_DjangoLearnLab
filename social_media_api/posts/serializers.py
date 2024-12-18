from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Post, Comment, Like



# --------------------------------------------  POST, COMMENT CRUD START ------------------------------------

# SERIALIZER CLASS FOR THE POST
class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']



# SERIALIZER CLASS FOR THE COMMENT
class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')  # Display username
    post_title = serializers.ReadOnlyField(source='post.title')  # Display post title for reference
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_username', 'post', 'post_title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

# --------------------------------------------  POST, COMMENT CRUD END ------------------------------------


# _______++++++++++ LIKES SECTION +++++++++________

# SERIALIZERS CLASS FOR LIKES
class LikeSerializer(serializers.ModelSerializer):
    user_like_username = serializers.ReadOnlyField(source='user.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Like
        fields = ['id', 'post', 'post_title', 'user_like_username']