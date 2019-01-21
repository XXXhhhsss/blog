from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from user.forms import RegisterForm,LoginFrom
from user.models import User


def index(request):
    if request.method == 'GET':
        return render(request,'back/index.html')

def login(request):
    if request.method =='GET':
        return render(request,'back/login.html')

    if request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('user:index'))
        else:
            errors = form.errors
            return render(request,'back/login.html',{'errors':errors})


def register(request):
    if request.method == 'GET':
        return render(request,'back/register.html')

    if request.method == 'POST':
        # 使用表单form做校验
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 账号不存在与数据库，密码和确认密码一致
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['pwd'])
            User.objects.create(
                username = username,
                password = password
            )
            return HttpResponseRedirect(reverse('user:login'))
        else:
            # 获取表单验证不通过的信息
            errors = form.errors
            return render(request,'back/register.html',{'errors':errors})

def logout(request):
    if request.method == 'GET':
        # 删掉session中的键值对user_id
        del request.session['user_id']
        return HttpResponseRedirect(reverse('user:login'))