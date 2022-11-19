from django.db import models

# Create your models here.

class student_details(models.Model):
    username = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    passwordtodb = models.CharField(max_length=20)
    emailid = models.CharField(max_length=50)



    