from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^list/$', views.list, name='list'),
]
