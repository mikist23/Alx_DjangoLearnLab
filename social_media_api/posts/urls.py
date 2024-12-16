from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

 

# -----------_____________USING VIEWSETS ___________________---------------------

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [

   
    path('', include(router.urls)),
]





# -----------_____________USING GENERICS ___________________---------------------
# from django.urls import path
# from .views import (
#     PostListCreateView, 
#     PostDetailView, 
#     CommentListCreateView, 
#     CommentDetailView
# )

# urlpatterns = [
#     path('posts/', PostListCreateView.as_view(), name='post-list-create'),
#     path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
#     path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
# ]