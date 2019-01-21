from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import random

#用户登录
def loginView(request):
    # 设置两个标题和另外两个连接
    title = '登录'
    #unit_2 = '/register.html'
    #unit_2_name = '立即注册'
    unit_1 = '/setpassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/index.html')
            else:
                tips = '账号密码错误，请重新输入'

        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())

#用户注册
def registerView(request):
    #设置标题和另外两个连接
    title = '注册'
    unit_2 = '/login.html'
    unit_2_name = '立即登录'
    unit_1 = '/setpassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            tips = '用户已存在'
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            tips = '注册成功，请登录'
    return render(request, 'user.html', locals())

#修改密码
def setpasswordView(request):
    #设置标题和另外两个连接
    title = '修改密码'
    unit_2 = '/login.html'
    unit_2_name = '立即登录'
    #unit_1 = '/register.html'
    #unit_1_name = '立即注册'
    new_password = True
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            user.set_password(new_password)
            user.save()
            tips = '密码修改成功'
        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())

#主页
def indexView(request):
    #获取当前请求的用户名
    username = request.user.username
    return render(request, 'index.html', locals())

#注销
def logoutView(request):
    logout(request)
    return redirect('index.html')