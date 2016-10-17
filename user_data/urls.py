from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login',views.login , name = 'login'),
    url(r'signup',views.signup , name = 'signup'),
    url(r'verified',views.verified , name = 'verified'),
	url(r'change' , views.change , name='change'),
	url(r'sendvericode' , views.sendveri , name='sendveri'),
    url(r'logout' , views.logout , name='logout'),
    url(r'req' , views.req , name='req'),
    url(r'view' , views.view , name='view'),
    url(r'sold' , views.sold , name='sold'),
    url(r'delete' , views.delete , name='delete'),
    url(r'details' , views.details , name='details'),
    ]
