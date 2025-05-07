from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_f, name='loging_page'),
    path('register/', views.register_f, name='register_page'),
]