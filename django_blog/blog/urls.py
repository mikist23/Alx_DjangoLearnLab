from django.urls import path
from .views import register_user

urlpatterns = [
    
    path('register/', register_user, name='register'),
    path('home/', register_user, name='home'),
    path('posts/', register_user, name='posts'),
    path('login/', register_user, name='login'),

]