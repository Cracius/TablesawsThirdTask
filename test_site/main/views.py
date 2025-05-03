from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.urls import reverse
from django.contrib import messages

def login_f(request):
    info = request.GET.get('info')
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user: User = User.objects.filter(login=form.cleaned_data['login']).first()
            if user:
                if form.cleaned_data['password'] == user.password:
                    return HttpResponse(f"Успешный вход для {user.login}!")
                else: error = 'Неверный пароль'
            else: error = 'Пользователь не найден'
        else: error = 'Форма заполнена неверно'
    else: form = UserForm()
    return render(request, 'main/login.html', {
        'form': form,
        'info': info,
        'error': error,
    })

def register_f(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user: User = User.objects.filter(login=form.cleaned_data['login']).first()
            if user: error = 'Данный логин занят'
            else:
                User.objects.create(login=form.cleaned_data['login'], password=form.cleaned_data['password'])
                return redirect(f"{reverse('loging_page')}?info=1")
        else: error = 'Форма заполнена неверно'
    else: form = UserForm()
    return render(request, 'main/register.html', {
        'form': form,
        'error': error,
    })