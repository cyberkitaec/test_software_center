from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator

# Create your models here.

# Кастомный AccountManager, с помощью него можно будет создавать юзера. В том числе и superuser
class AccountManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError('такой пользователь уже существует')

        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Переопределим создание superuser`a. Т.к. если мы будем создавать его через create_user
    # то получится что мы хэшируем пароль superuser`a два раза, т.к. по дефолту он хэшируется автоматически.
    def create_superuser(self, login, email=None, password=None, **extra_fields):
        return User.objects.create(login=login, password=password, is_staff = True, is_admin = True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):

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
    date_of_registration = models.DateField(u'Дата регистрации', auto_created=True, blank=True, auto_now_add=True)
    date_of_birthday = models.DateField(u'Дата рождения', blank=True, null=True, default=None)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = None

    USERNAME_FIELD = 'login'
    objects = AccountManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'
    #
    # Хешируем пароль. По умолчанию это SHA256
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    # @property
    # def is_staff(self):
    #     return self.is_admin



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


