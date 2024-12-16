from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


User = get_user_model()

# --------------------------------------------  USER CRUD START ------------------------------------

# SERIALIZER CLASS FOR REGISTERING NEW USERS
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
             username = validated_data['username'],
             email = validated_data.get('email', ''),
             password= validated_data['password'],
             bio = validated_data.get('bio',''),
             profile_picture = validated_data.get('profile_picture', None),
             
        )

         # Generate token for the user
        Token.objects.create(user=user)

        return user
    
    def to_representation(self, instance):
        """Add token to the response."""
        representation = super().to_representation(instance)
        token = Token.objects.get(user=instance)
        representation['token'] = token.key  # Append the token
        representation.pop('password', None)  # Ensure password is not included in the response
        return representation
    
# SERIALIZER CLASS FOR LISTING ALL THE USERS
class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture'] 


# SERIALIZER CLASS FOR LISTING ALL THE USERS
class DeleteUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture'] 
        
# SERIALIZER CLASS FOR TOKEN GENERATION
class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

# SERIALIZER CLASS FOR USER PROFILE
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']
        read_only_fields = ['id', 'username']  # Prevent updates to certain fields


# --------------------------------------------  USER CRUD END ------------------------------------

