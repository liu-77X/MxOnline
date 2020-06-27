from django.conf.urls import url
from apps.organizations.views import OrgView, AddAsk, TeacherListView, TeacherDeatailView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='list'),
    #添加一个请求
    url(r'^add_ask/$', AddAsk.as_view(), name='add_ask'),

]
