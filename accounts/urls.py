from django.urls import path
from .views import UserRegistrationView, LoginView, UpdateProfileView



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('profile/', UpdateProfileView.as_view(), name = 'profile')
]