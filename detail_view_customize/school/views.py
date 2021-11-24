from django.shortcuts import render
from .models import student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
class StudentDetailView(DetailView):
    model = student
    template_name = 'school/student.html'
    context_object_name = 'stu'
    pk_url_kwarg = 'id'


class StudentListView(ListView):
    model = student