import string
from errno import ELOOP
from string import whitespace

from django.contrib.auth import authenticate, login, get_user_model
from .models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json

User = get_user_model()

def invalid(value: str) -> bool:
    return value in ('', None, Ellipsis) or value.strip() == ''

def login_f(request) -> HttpResponse:
    if request.method == 'POST':
        form = json.loads(request.body)
        username: str = form.get('username')
        password: str = form.get('password')

        if invalid(username) or invalid(password):
            return JsonResponse({'status': 'err', 'inf': 'Некорректный ввод данных'})

        user: User = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'status': 'ok', 'inf': f'Успешный вход пользователя {user.username}'})
        return JsonResponse({'status': 'err', 'inf': 'Неверный логин или пароль'})
    return render(request, 'main/login.html', { 'user': request.GET.get('user') })

def register_f(request) -> HttpResponse:
    if request.method == 'POST':
        form = json.loads(request.body)
        username: str = form.get('username')
        password: str = form.get('password')
        gender: bool = form.get('gender')

        if invalid(username) or invalid(password):
            return JsonResponse({'status': 'err', 'inf': 'Некорректный ввод данных'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'err', 'inf': 'Пользователь с таким логином уже существует'})

        User.objects.create_user(username=username, password=password, gender=gender)
        return JsonResponse({'status': 'ok', 'inf': f'/?user={username}'})
    return render(request, 'main/register.html')