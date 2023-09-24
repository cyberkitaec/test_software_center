from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login', UserLoginView.as_view(), name='login'),
    path('registration', UserRegisterView.as_view(), name='register'),
    path('logout', UserLogoutView.as_view(), name='logout'),
]
