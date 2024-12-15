from django.urls import path
from .views import RegistrationView, LoginView, ListUsersView

urlpatterns = [

    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('list_users/', ListUsersView.as_view(), name='list_users' ),

]