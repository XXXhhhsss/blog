import re

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect


class LoginMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # 拦截请求之前的函数
        # 1.给request.user属性赋值，赋值为当前登录系统的用户
        user_id = request.session.get('user_id')
        #取不到user_id值，在，直接返回登录页面
        path = request.path
        not_need_check = ['/user/login/','/user/register/']
        for check_path in not_need_check:
            if re.match(check_path,path):
                return None
        if not user_id:
            return  HttpResponseRedirect(reverse('user:login'))



