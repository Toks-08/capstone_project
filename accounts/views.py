from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, LoginSerializer, UserProfileSerializer, UpdateProfileSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserRegistrationView(CreateAPIView):
    model = User
    serializer_class = UserRegistrationSerializer


class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response ({
            'message':'login successful',
            'token': token.key,
            'user':{
                'id': user.id,
                'username': user.username,
                'email':user.email
            }
        }, status = status.HTTP_200_OK)

class ProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user

class UpdateProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

