from django.contrib import admin
from .models import cardetails
# Register your models here.
class Car_admin_details(admin.ModelAdmin):
    list_display = ('car_number','car_address','car_name','car_year')
admin.site.register(cardetails,Car_admin_details)
