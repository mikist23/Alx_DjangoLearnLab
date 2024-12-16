from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
from django.utils import timezone

# Create your models here.
# MODEL CLASS FOR POSTS
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # Use AUTH_USER_MODEL here
    title = models.CharField(max_length=200, default="Default post title")
    content = models.TextField()
    created_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# MODEL CLASS FOR COMMENT
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # Use AUTH_USER_MODEL here
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"