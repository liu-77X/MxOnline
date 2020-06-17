from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from apps.users.form import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# from apps.users.models import UserProfile
# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        next = request.GET.get("next", "")
        return render(request, 'login.html', {"next": next})
    def post(self, request, *args, **kwargs):
        """
        用户登录验证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 实例化 LoginForm
        login_form = LoginForm(request.POST)
        # 判断是否合法
        if login_form.is_valid():
            # 用于通过用户名和密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # 认证给出的用户名和密码，使用 authenticate() 函数。它接受两个参数，用户名 username 和 密码 password ，并在密码对给出的用户名合法的情况下返回一个 User 对象。 如果密码不合法，authenticate()返回None。
            user = authenticate(username=user_name, password=password)
            # 判断user对象是否存在
            if user is not None:
                # 不为空， z证明查询到了用户
                login(request, user)
                # 取一下next值
                next = request.GET.get("next", "")
                if next:
                    return HttpResponseRedirect(next)
                # 重定向到网站首页
                return HttpResponseRedirect(reverse("index"))
            else:
                # 未查询到用户，要求重新登录,仍然返回login界面
                return render(request, 'login.html', {"msg": "用户名密码错误", "login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        # 重定向到网站首页
        return HttpResponseRedirect(reverse("index"))
class UserInfoView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        current_page = 'info'
        return render(request, 'usercenter-info.html', {
            "current_page": current_page
        })
