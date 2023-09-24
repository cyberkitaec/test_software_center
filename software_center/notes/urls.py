from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('user/registration', UserRegistrationView.as_view()),
    path('event', EventView.as_view()),
    path('event/detail/<int:pk>', EventDetailView.as_view()),
    path('event/delete/<int:pk>', EventDeleteView.as_view()),
    path('user/remove/event', RemoveUserFromEventView.as_view()),
    path('user/add/event', AddUserToEventView.as_view()),
]
