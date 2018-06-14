from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^mypath/$', views.MyView.as_view(), name='myview'),
]
