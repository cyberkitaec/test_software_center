from django.db import models

# Create your models here.



# Сущность "Пользователь"
class User(models.Model):

    login = models.CharField(u'Логин',max_length=30)
    password = models.CharField(max_length=20)
    name = models.CharField(u'Имя', max_length=30)
    surname = models.CharField(u'Фамилия', max_length=30)
    date_of_registration = models.DateField(u'Дата регистрации')
    date_of_birthday = models.DateField(u'Дата рождения', null=True)

    #
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'


# Сущность "Событие"
class Event(models.Model):
    title = models.CharField(u'Заголовок', max_length=150)
    desc = models.CharField(u'Текст', max_length=300)
    date_of_create = models.DateField(u'Дата создания')
    creator = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Создатель', related_name='creator2user')
    participants = models.ManyToManyField('User', verbose_name='Участники', related_name='participants2user')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Событие'

