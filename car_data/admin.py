from django.contrib import admin
from .models import Car_data_new , Varient_data , Car_data_old

admin.site.register(Car_data_new)
admin.site.register(Varient_data)
admin.site.register(Car_data_old)