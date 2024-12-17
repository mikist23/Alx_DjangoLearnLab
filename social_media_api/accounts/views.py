from django.shortcuts import render
from .serializers import RegistrationSerializer,  ListUsersSerializer, TokenSerializer, DeleteUserSerializer, UserProfileSerializer
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
    



# ------------------_________________________FOLLOWERS SECTION_______________________-----------------------------

