"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
from MxOnline.settings import MEDIA_ROOT
from apps.courses.views import CourseListView
from apps.organizations.views import OrgView
from apps.users.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # path('', views.index),
    path('', TemplateView.as_view(template_name="index.html"),name='index'),
    path('course-list/',CourseListView.as_view(), name='course-list'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(), name ='logout'),
    #配置授课机构表展示
    # path('org_list/', OrgView.as_view(),name='org_list'),
    # 配置上传文件的访问url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 课程相关页面
    url(r'^course/', include(('apps.courses.urls', 'courses'), namespace='course')),
    # 授课机构相关配置,跳转到org下面的url
    url(r'^org/', include(('apps.organizations.urls', 'organizations'), namespace='org')),


]
