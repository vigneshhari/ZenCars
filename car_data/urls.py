from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'search',views.search , name = 'search'),
    url(r'add',views.viewadd , name = 'viewadd'),
    url(r'processnew',views.add , name = 'add'),
    url(r'view',views.view , name = 'view'),
    url(r'comm',views.comm , name = 'comm'),

    ]
