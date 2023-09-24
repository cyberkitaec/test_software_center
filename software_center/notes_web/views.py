from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'notes_web/html/index.html')


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