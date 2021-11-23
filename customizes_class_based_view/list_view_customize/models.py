from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    roll = models.IntegerField()
    course = models.CharField(max_length=100)
    