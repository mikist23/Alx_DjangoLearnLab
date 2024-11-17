from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        
        user = self.model(
            email=email,
            date_of_birth=date_of_birth,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
          
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, date_of_birth, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name= 'email address',
        max_length=255,
        unique=True
    )
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(null=True, blank=True)
    username = None
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email
    