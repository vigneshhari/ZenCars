

from django.contrib import admin
from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('user_data.urls')),
 	url(r'^home/', views.home),   
]
