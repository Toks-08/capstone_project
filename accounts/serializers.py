from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.serializers import ValidationError
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']



    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError ("Password Fields Does Not Match")
        return attrs



    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, validated_data):
        user = authenticate(**validated_data)
        if not user:
            raise serializers.ValidationError("Invalid Username Or Password")
        validated_data['user']=user
        return validated_data

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'phone_number', 'address_line1', 'address_line2',
            'city', 'state', 'country', 'postal_code'
        ]

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits")
        return value

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id',]

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': False}
        }