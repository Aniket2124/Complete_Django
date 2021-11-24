from django.shortcuts import render
from .models import student
from django.views.generic.detail import DetailView

# Create your views here.
class StudentDetailView(DetailView):
    model = student