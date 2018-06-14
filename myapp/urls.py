from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^mypath/$', views.MyView.as_view(), name='myview'),
    url(r'^create/$', views.MyView.as_view(), name='mycreateview'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.MyUpdateView.as_view(), name='myupdateview'),

]
