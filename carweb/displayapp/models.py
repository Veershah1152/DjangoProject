from django.db import models

class cardetails(models.Model):
    car_number = models.CharField(max_length=10)
    car_address =models.CharField()
    car_name = models.CharField()
    car_year = models.IntegerField()
