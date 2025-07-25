from django.db import models

# Create your models here.

class Profile(models.Model): 
    name  = models.CharField(max_length=200)
    previous_work  = models.CharField(max_length=2000)
    school  = models.CharField(max_length=200)
    university  = models.CharField(max_length=200)
    skills  = models.TextField(max_length=2000)
    summary  = models.TextField(max_length=200)
    email  = models.CharField(max_length=200)
    phone  = models.CharField(max_length=200)
    degree  = models.CharField(max_length=2000)