from django.conf.urls import url
from apps.organizations.views import OrgView, AddAsk, TeacherListView, TeacherDeatailView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='list'),
]
