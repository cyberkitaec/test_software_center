from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    """
    Админка пользователя. В админке не будет отоброжаться password юзера
    """
    list_display = ['id', 'name', 'surname', 'date_of_registration', 'date_of_birthday']
    list_display_links = ['id', 'name', 'surname', 'date_of_registration', 'date_of_birthday']
    search_fields = ['id', 'name', 'surname', 'date_of_registration', 'date_of_birthday']


class EventAdmin(admin.ModelAdmin):
    """
    Админка событий.
    """
    list_display = '__all__'
    list_display_links = '__all__'
    search_fields = '__all__'


# Регистрируем админки

admin.site.register(User)
admin.site.register(Event)
