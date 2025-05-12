from django.db.models import CharField, BooleanField, Model, CASCADE, OneToOneField, BinaryField
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    password: CharField = CharField('Пароль', max_length=100)
    gender: BooleanField = BooleanField('Пол (не ламинат)', default=True)

    class Meta:
        db_table: str = 'users'
        verbose_name: str = 'Пользователя'
        verbose_name_plural: str = 'Пользователи'

    def __str__(self):
        return self.username

class Avatar(Model):
    user: OneToOneField = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    img: BinaryField = BinaryField('Изображение')

    class Meta:
        db_table: str = 'avatars'
        verbose_name: str = 'Аватар'
        verbose_name_plural: str = 'Аватары'