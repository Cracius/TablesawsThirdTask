from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_f, name='loging_page'),
    path('register/', views.register_f, name='register_page'),
    path('home/', views.home_f, name='home'),
    path('logout/', views.logout_f, name='logout'),
]