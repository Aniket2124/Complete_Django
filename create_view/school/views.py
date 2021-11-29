from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','password']
    # for redirecting Template
    # success_url = '/thanks/'


    # Or u can use method get_absolute_url in models.py

class StudentTemplateView(TemplateView):
    template_name = 'school/thanks.html'


class StudentDetailView(DetailView):
    model = Student
