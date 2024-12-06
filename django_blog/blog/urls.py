from django.urls import path
from .views import (
    register_user, 
    login_user,
    profile,
    CreatePost,
    UpdatePost,
    DeletePost,
    DetailPost,
    ListPost
    )

urlpatterns = [
    
    path('register/', register_user, name='register'),
    path('home/', register_user, name=''),

    path('posts/', ListPost.as_view(), name='list_post'),
    path('posts/<int:id>/', DetailPost.as_view(), name='detail_post'),
    path('posts/new/', CreatePost.as_view(), name='create_post'),
    path('posts/<int:id>/edit', UpdatePost.as_view(), name='update_post'),
    path('posts/<int:id>/delete', DeletePost.as_view(), name='delete_post'),

    path('login/', login_user, name='login'),
    path('profile/', profile, name='profile'),
    

]