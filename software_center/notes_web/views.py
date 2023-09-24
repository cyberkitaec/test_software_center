from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, View, DeleteView
from django.db.models import Q
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from .forms import *
from django.http import JsonResponse, HttpResponse
from notes.models import *
from notes.serializers import *

# Create your views here.

def index(request):
    id = request.user.id
    ser = EventDataSerializer(Event.objects.filter(creator=id), many=True)
    all_events = EventDataSerializer(Event.objects.all(), many=True)
    return render(request, 'notes_web/html/index.html', {"queryset": ser.data, "all_events": all_events.data})



# Для ajax
class GetAllEvents(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(EventSerializer(Event.objects.all(), many=True).data,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False})

class DetailOfEventView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(EventDataSerializer(Event.objects.get(pk=kwargs['pk'])).data,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False})


class MyEventsView(View):

    def get(self, request, *args, **kwargs):
        id = request.user.id
        ser = EventDataSerializer(Event.objects.filter(Q(participants__in = [id]) | Q(creator=id)), many=True)
        return JsonResponse(ser.data,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False})


class InsertUserToEventView(View):
    """
    Представление для добавление нового пользователя в ивент
    """
    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=kwargs['pk'])
        user = User.objects.get(id=request.user.id)
        event.participants.add(user)
        return HttpResponse(200)


class RemoveUserFromEventView(View):

    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=kwargs['pk'])
        user = User.objects.get(id=request.user.id)
        event.participants.remove(user)
        return HttpResponse(200)

@method_decorator(csrf_exempt, name='dispatch')
class DeleteEventView(View):
    def delete(self, request, *args, **kwargs):
        event = Event.objects.get(id=kwargs['pk'])
        event.delete()
        event.save()
        return HttpResponse(200)


class UserDataView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(UserM2mSerializer(User.objects.get(id=kwargs['pk'])).data,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False})

class UserLoginView(LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'notes_web/html/login.html'
    next_page = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class UserRegisterView(CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    redirect = reverse_lazy('index')
    template_name = 'notes_web/html/registration.html'

    def form_valid(self, form):
        """
        После регистрации сразу будем логиниться
        """
        valid = super().form_valid(form)
        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return valid

    def get_success_url(self):
        return reverse('index')

class UserLogoutView(LogoutView):
    """
    Выход с сайта
    """
    next_page = 'index'