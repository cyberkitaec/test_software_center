from .models import *
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UserM2mSerializer(ModelSerializer):
    """
    Сериализер который будет нам возращать только нужные данные из модели User
    """

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'date_of_registration', 'date_of_birthday']


class EventSerializer(ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        m2m_data = validated_data.pop('participants')
        instance = Event.objects.create(**validated_data)
        instance.participants.set(m2m_data)
        return instance

class EventDataSerializer(ModelSerializer):
    """
    Возвращает все данные из ивент + полную дату юзеров (за исключением пароля)
    """
    name_creator = serializers.CharField(source='creator.name')
    surname_creator = serializers.CharField(source='creator.surname')
    participants = UserM2mSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'desc', 'date_of_create', 'name_creator', 'surname_creator', 'participants', 'creator']
