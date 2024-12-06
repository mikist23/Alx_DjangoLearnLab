from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'image', 'created_at', 'updated_at']