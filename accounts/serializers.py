from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class UserRegistrationSerializers(serializers.ModelSerializer):
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

class UserProfileSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'email', 'first_name', 'last_name']
    read_only_fields = ['id',]

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': False}
        }