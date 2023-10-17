from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    status=models.BooleanField(default=False)



# class MyModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.TextField()

#     def __str__(self):
#         return self.field1

class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.PositiveIntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linkedin_url = models.URLField()
    current_employee_estimate = models.PositiveIntegerField()
    total_employee_estimate = models.PositiveIntegerField()