from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import *
from .serializers import *

# Create your views here.

class UserRegistrationView(CreateAPIView):
    """
    регистрация юзера
    """
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response({"error": None, "result": HTTP_200_OK}, status=HTTP_200_OK)


class EventView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        """
        Список всех событий
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        event_serializer = EventDataSerializer(Event.objects.all(), many=True)
        return Response({"error": None, "result": event_serializer.data}, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Создание события
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        event_serializer = EventSerializer(data=request.data)
        event_serializer.is_valid(raise_exception=True)
        event_serializer.save()

        return Response({"error": None, "result": HTTP_200_OK}, status=HTTP_200_OK)


class EventDetailView(ListAPIView):
    """
    Получаем дату события по его id
    """
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        try:
            detail_event = Event.objects.get(pk=kwargs['pk'])
        except:
            return Response({"error": HTTP_404_NOT_FOUND, "result": "Object not found"}, status=HTTP_404_NOT_FOUND)

        return Response({"error": None, "result": EventDataSerializer(detail_event).data})


class EventDeleteView(DestroyAPIView):
    """
    Удаление события
    """
    permission_classes = [IsAuthenticated, ]
    
    def delete(self, request, *args, **kwargs):
        try:
            object_to_delete = Event.objects.get(pk=kwargs['pk'])
        except:
            return Response({"error": HTTP_404_NOT_FOUND, "result": "Object not found"}, status=HTTP_404_NOT_FOUND)

        object_to_delete.delete()
        object_to_delete.save()

        return Response({"error": None, "result": HTTP_200_OK}, status=HTTP_200_OK)


class AddUserToEventView(APIView):

    def post(self, request, *args, **kwargs):
        if not Event.objects.filter(id=request.data['event_id']).exists():
            return Response({"error": HTTP_404_NOT_FOUND, "result": "Event object not found"}, status=HTTP_404_NOT_FOUND)
        event = Event.objects.filter(id=request.data['event_id'])
        if not User.objects.filter(id=request.data['user_id']).exists():
            return Response({"error": HTTP_404_NOT_FOUND, "result": "User object not found"}, status=HTTP_404_NOT_FOUND)
        user = User.objects.get(id=request.data['user_id'])
        event.participants.add(user)
        return Response({"error": None, "result": HTTP_200_OK})

class RemoveUserFromEventView(APIView):
    def post(self, request, *args, **kwargs):
        if not Event.objects.filter(id=request.data['event_id']).exists():
            return Response({"error": HTTP_404_NOT_FOUND, "result": "Event object not found"}, status=HTTP_404_NOT_FOUND)
        event = Event.objects.get(id=request.data['event_id'])
        if not User.objects.filter(id=request.data['user_id']).exists():
            return Response({"error": HTTP_404_NOT_FOUND, "result": "User object not found"}, status=HTTP_404_NOT_FOUND)
        user = User.objects.get(id=request.data['user_id'])
        event.participants.remove(user)
        return Response({"error": None, "result": HTTP_200_OK})


