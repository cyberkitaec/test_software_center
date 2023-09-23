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
    # m2m field not supported
    list_display = ['id', 'title', 'desc', 'date_of_create', 'creator',]
    list_display_links = ['id', 'title', 'desc', 'date_of_create', 'creator',]
    search_fields = ['id', 'title', 'desc', 'date_of_create', 'creator',]


# Регистрируем админки

admin.site.register(User, UserAdmin)
admin.site.register(Event, EventAdmin)
