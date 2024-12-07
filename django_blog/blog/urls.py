from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    register_user, 
    login_user,
    profile,
    CreatePost,
    UpdatePost,
    DeletePost,
    DetailPost,
    ListPost,
    CommentUpdateView,
    CommentDeleteView,
    search_posts,
    PostByTagListView
    )

urlpatterns = [
    
    path('register/', register_user, name='register'),
    path('home/', register_user, name='home'),
    path('pos/', ListPost.as_view(), name='posts'),

    path('posts/', ListPost.as_view(), name='list_post'),
    path('posts/<int:pk>/', DetailPost.as_view(), name='detail_post'),
    path('post/new/', CreatePost.as_view(), name='create_post'),
    path('post/<int:pk>/update/', UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='delete_post'),
    path('post/<int:pk>/comments/new/', ListPost.as_view(), name='posts'),
    


    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update' ),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete' ),

    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_name>/', PostByTagListView.as_view(), name='posts_by_tag'),


    path('login/', login_user, name='login'),
    path('profile/', profile, name='profile'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)