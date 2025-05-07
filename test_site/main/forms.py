from django.forms import TextInput, PasswordInput, CharField, Form, ModelForm
from .models import User

class RegisterForm(ModelForm):
    username = CharField(label="Логин", max_length=100, widget=TextInput(attrs={
        'placeholder': 'Логин'
    }))

    password = CharField(label="Пароль", max_length=100, widget=PasswordInput(attrs={
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ['username', 'password', 'gender']

class LoginForm(Form):
    username = CharField(label="Логин", max_length=100, widget=TextInput(attrs={
        'placeholder': 'Логин'
    }))

    password = CharField(label="Пароль", max_length=100, widget=PasswordInput(attrs={
        'placeholder': 'Пароль'
    }))