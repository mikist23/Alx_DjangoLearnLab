from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
from django.utils import timezone

# Create your models here.
# User = get_user_model()

# MODEL CLASS FOR CREATING CUSTOM USER MODEL
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='user_followers', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_following', blank=True)

    def __str__(self):
        return self.username
    

