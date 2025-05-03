from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField('Логин', max_length=100, unique=True)
    password = models.CharField('Пароль', max_length=100)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.login