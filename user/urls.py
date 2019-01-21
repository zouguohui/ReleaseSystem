from django.urls import path
from . import views

urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('register.html', views.registerView, name='register'),
    path('setpassword.html', views.setpasswordView, name='setpassword'),
    path('index.html', views.indexView, name='index'),
    path('logout.html', views.logoutView, name='logout'),
]