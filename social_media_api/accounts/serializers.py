from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'email', 'bio')
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate(self, data):
        """
        Validates that the two password fields match.
        """
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        """
        Creates and returns a new user instance, given the validated data.
        """
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the user's profile.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')
        read_only_fields = ('username', 'email')
