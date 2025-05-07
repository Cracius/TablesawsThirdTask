from django.db.models import CharField, BooleanField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    password = CharField('Пароль', max_length=100)
    gender = BooleanField('Пол (не ламинат)', default=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username