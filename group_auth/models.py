from datetime import date

from django.contrib.auth.models import AbstractUser, Group
from django.db import models

STREET = (
    ('SARAN', 'Сарань'),
    ('KAZ_BY', 'Казыбек Би'),
    ('BUKEY', 'Букейханов'),
    ('MAIKEN', 'Майкудук'),
    ('JBI', 'ЖБИ'),
    ('SHAHTINSK', 'Шахтинск'),
    ('ABAY', 'Абай'),
    ('TEMIRTAU', 'Темиртау'),
)


class Users(AbstractUser):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    phone = models.PositiveIntegerField('Номер телефона', default=7)
    city = models.CharField('Город', choices=STREET, default='KAZ_BY', max_length=100)
    job_title = models.CharField('Должность', max_length=120)
    iin = models.PositiveIntegerField('ИИН', default=7)
    groups = models.ManyToManyField(Group, verbose_name='Группа')
    USERNAME_FIELD = 'username'


class CustomGroup(Group):
    users = models.ManyToManyField(Users, null=True, blank=True, verbose_name='Пользователи')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
