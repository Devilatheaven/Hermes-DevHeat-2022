from django.db import models

# Create your models here.

class student_details(models.Model):
    username = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    passwordtodb = models.CharField(max_length=20)
    emailid = models.CharField(max_length=50)

class teacher_details(models.Model):
    tfirstname = models.CharField(max_length=100)
    tlastname = models.CharField(max_length=100)
    temail = models.CharField(max_length=100)
    tphone = models.CharField(max_length=100)
    tpassword = models.CharField(max_length=100)

class doubts(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=10000)
    