from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator

# Create your models here.


# Сущность "Пользователь". Создаем свою base-model на основе AbstractBaseUser для корректной работы JWT
class User(AbstractBaseUser):

    login = models.CharField(u'Логин',max_length=30, unique=True)
    password = models.CharField(max_length=128,
                                validators=[
                                    RegexValidator(
                                        regex='^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                                        message='Не меньше 8 символов. Пароль должен содержать одну букву и одну цифру'
                                    )
                                ]

                                )
    name = models.CharField(u'Имя', max_length=30)
    surname = models.CharField(u'Фамилия', max_length=30)
    date_of_registration = models.DateField(u'Дата регистрации')
    date_of_birthday = models.DateField(u'Дата рождения', blank=True, null=True, default=None)
    is_staff = models.BooleanField(default=False)
    last_login = None

    USERNAME_FIELD = 'login'
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'

    # Хешируем пароль. По умолчанию это SHA256
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def natural_key(self):
        return self.name


# Сущность "Событие"
class Event(models.Model):
    title = models.CharField(u'Заголовок', max_length=150)
    desc = models.CharField(u'Текст', max_length=300)
    date_of_create = models.DateField(u'Дата создания', auto_created=True, blank=True, auto_now_add=True)
    creator = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Создатель', related_name='creator2user')
    participants = models.ManyToManyField('User', verbose_name='Участники', related_name='participants2user')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Событие'

    def natural_key(self):
        return self.name


