from django.urls import path
from .views import RegistrationView, LoginView, ListUsersView, DeleteUserView, UserProfileView

urlpatterns = [

    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('list_users/', ListUsersView.as_view(), name='list_users' ),
    path('delete_user/', DeleteUserView.as_view(), name='delete_user' ),
    path('profile/', UserProfileView.as_view(), name='profile'),

]