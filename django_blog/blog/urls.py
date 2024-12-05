from django.urls import path
from .views import register_user, login_user,profile

urlpatterns = [
    
    path('register/', register_user, name='register'),
    path('home/', register_user, name='home'),
    path('posts/', register_user, name='posts'),
    path('login/', login_user, name='login'),
    path('profile/', profile, name='profile'),
    

]