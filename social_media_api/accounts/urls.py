from django.urls import path
from .views import RegistrationView, LoginView, ListUsersView, DeleteUserView, UserProfileView, FollowUserView, UnfollowUserView, UserFollowingListView

urlpatterns = [
     
    # _____________---------+++++___URLS FOR CUSTOM USER_____________---------+++++___
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('list_users/', ListUsersView.as_view(), name='list_users' ),
    path('delete_user/', DeleteUserView.as_view(), name='delete_user' ),
    path('profile/', UserProfileView.as_view(), name='profile'),


    # _____________---------+++++___URLS FOR FOLLOWERS (generics/apiview)_____________---------+++++___
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('following/', UserFollowingListView.as_view(), name='user-following'),

]