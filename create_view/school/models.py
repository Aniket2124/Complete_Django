from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)


    # for redirecting to template

    def get_absolute_url(self):
        return reverse("thanks")


    # use this code for showing details after login
    def get_absolute_url(self):
        return reverse('details', kwargs={'pk':self.pk})