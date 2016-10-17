from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'blog',views.blog , name = 'blog'),
    url(r'list',views.list , name = 'list'),
    url(r'comm',views.comm , name = 'comm'),

    ]
