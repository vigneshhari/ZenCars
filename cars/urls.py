
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('user_data.urls')),
    url(r'^car' , include('car_data.urls')),
    url(r'^blog' , include('blog.urls')),
 	url(r'^home/', views.home),   
 	url(r'^about/', views.about),   
 	url(r'^contact/', views.contact),   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
