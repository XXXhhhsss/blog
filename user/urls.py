from django.urls import path

from user import views

urlpatterns = [
    # 后台主页
    path('index/', views.index,name='index'),
    # 登录
    path('login/', views.login, name='login'),
    # 注册
    path('register/', views.register,name='register'),
    # 退出
    path('logout/',views.logout,name='logout'),

]