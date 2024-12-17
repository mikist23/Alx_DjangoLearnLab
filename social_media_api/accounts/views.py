from django.shortcuts import render
from .serializers import RegistrationSerializer, FollowSerializer, ListUsersSerializer, TokenSerializer, DeleteUserSerializer, UserProfileSerializer
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView

# Create your views here.

User = get_user_model()


# REGISTRATION VIEW CREATING NEW USER
class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

# LOG IN VIEW IMPLEMENTATION
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

         # Debugging
        print(f"Attempting login for: {username}")

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            print("Login successfull")
            return Response({'token': token.key}, status=200)
        return Response({'error':'Invalid credentials'}, status=400)
    


# LIST USER VIEW
class ListUsersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ListUsersSerializer


# DELETE USER VIEW
class DeleteUserView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = DeleteUserSerializer
    lookup_field = ['id']

    def get_object(self):
        # Ensure that the user can only delete themselves
        return self.request.user  # Return the authenticated user
    

# USER PROFILE VIEWS
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Retrieve the authenticated user's profile."""
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """Update the authenticated user's profile."""
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)  # Allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



# ------------------_________________________FOLLOWERS SECTION USING GENERICS VIEWS_______________________-----------------------------

# view for following a user

class FollowUserView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, *args, **kwargs):
        try:
            user_to_follow = self.get_object() #Get the user to follow
            if user_to_follow == request.user:
                return Response({'error': "You can not  follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            
            request.user.following.add(user_to_follow)
            return Response({"success": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)
    

        except CustomUser.DoesNotExist:
            return Response({'error': "User not found"}, status=status.HTTP_404_NOT_FOUND)

# view for unfollowing a user

class UnfollowUserView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        try:
            user_to_unfollow = self.get_object() #Get the user
            if user_to_unfollow == request.user:
                return Response({"error": "You can not unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            
            request.user.following.remove(user_to_unfollow)
            return Response({"success": f"You have unfollow {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
        
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        

# view for listing all users th current user is following
class UserFollowingListView(ListAPIView):
    
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following.all() #Retrive the users being followed
    















# ------------------_________________________FOLLOWERS SECTION USING APIVIEW_______________________-----------------------------

# # accounts/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from .models import CustomUser
# from .serializers import FollowSerializer

# class FollowUserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, user_id):
#         try:
#             user_to_follow = CustomUser.objects.get(pk=user_id)
#             if user_to_follow == request.user:
#                 return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            
#             request.user.following.add(user_to_follow)
#             return Response({"success": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)
#         except CustomUser.DoesNotExist:
#             return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

# class UnfollowUserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, user_id):
#         try:
#             user_to_unfollow = CustomUser.objects.get(pk=user_id)
#             if user_to_unfollow == request.user:
#                 return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

#             request.user.following.remove(user_to_unfollow)
#             return Response({"success": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
#         except CustomUser.DoesNotExist:
#             return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

# class UserFollowingListView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         following = request.user.following.all()
#         serializer = FollowSerializer(following, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
