from django.contrib.auth import authenticate, login, get_user_model, logout
from django.core.files.images import ImageFile
from .models import User, Avatar
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings
from os.path import join
from json import loads
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from base64 import b64encode
from django.urls import reverse

User: User = get_user_model()

def invalid(value: str) -> bool:
    return value in ('', None, Ellipsis) or value.strip() == ''

def login_f(request) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponse(f"""
            <h1>Вы уже вошли</h1>
            <a href="{reverse('home')}">На домашнюю страницу</a>
        """)

    if request.method == 'POST':
        form: dict = loads(request.body)
        username: str = form.get('username')
        password: str = form.get('password')

        if invalid(username) or invalid(password):
            return JsonResponse({'status': 'err', 'inf': 'Некорректный ввод данных'})

        user: User = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({ 'status': 'ok', 'inf': '/home/' })
        return JsonResponse({'status': 'err', 'inf': 'Неверный логин или пароль'})
    return render(request, 'main/login.html', { 'user': request.GET.get('user') })

def register_f(request) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponse(f"""
            <h1>Вы уже вошли</h1>
            <a href="{reverse('home')}">На домашнюю страницу</a>
        """)

    if request.method == 'POST':
        username: str = request.POST.get('username')
        password: str = request.POST.get('pass')
        gender: bool = request.POST.get('gender') == 'Male'

        if invalid(username) or invalid(password):
            return JsonResponse({'status': 'err', 'inf': 'Некорректный ввод данных'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'err', 'inf': 'Пользователь с таким логином уже существует'})

        img_file: ImageFile = request.FILES.get('avatar')
        path = join(settings.BASE_DIR, 'main/static/main/img/avatar.jpg')
        img = img_file.read() if img_file else open(path, 'rb').read()

        user: User = User.objects.create_user(username=username, password=password, gender=gender)
        Avatar.objects.create(user=user, img=img)
        return JsonResponse({'status': 'ok', 'inf': f'/?user={username}'})
    return render(request, 'main/register.html')

@login_required(login_url='loging_page')
@ensure_csrf_cookie
def home_f(request):
    avatar = None
    try: avatar = b64encode(request.user.avatar.img).decode('utf-8')
    except Exception as e: print(e)
    return render(request, 'main/home.html', { 'avatar': avatar })

@require_http_methods(["POST"])
def logout_f(request):
    logout(request)
    return JsonResponse({'status': 'ok', 'inf': 'logout'})