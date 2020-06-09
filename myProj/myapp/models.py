from django.db import models

# Create your models here.
class Teach(models.Model):
    Title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    time=models.CharField(null=True,max_length=10,blank=True)