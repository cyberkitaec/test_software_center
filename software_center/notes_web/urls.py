from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login', UserLoginView.as_view(), name='login'),
    path('registration', UserRegisterView.as_view(), name='register'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('update/all_events', GetAllEvents.as_view(), name='all_events'),
    path('update/event/<int:pk>', DetailOfEventView.as_view(), name='detail_event'),
    path('update/my_events', MyEventsView.as_view(), name='my_events'),
    path('events/user/delete/<int:pk>', DeleteEventView.as_view(), name='delete_user_event'),
    path('events/user/insert/<int:pk>', InsertUserToEventView.as_view(), name='insert_user_event'),
    path('events/user/remove/<int:pk>', RemoveUserFromEventView.as_view(), name='remove_user_event')
]
