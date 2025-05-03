from django.forms import TextInput, PasswordInput, CharField, Form

class UserForm(Form):
    login = CharField(label="Логин", max_length=100,
        widget=TextInput(attrs={
            'placeholder': 'Логин'
        })
    )
    password = CharField(label="Пароль", max_length=100,
        widget=TextInput(attrs={
            'placeholder': 'Пароль'
        })
    )