from django.db.models.base import Model
from django.shortcuts import render
from .models import student
from django.views.generic.list import ListView

# Create your views here.
class StudentListView(ListView):
    model = student

