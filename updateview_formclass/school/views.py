from django.db import models
from django.forms import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Student
from django.views.generic.base import TemplateView
from django import forms
from.forms import StudentForm

# Create your views here.
# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name','email','password']
#     # for redirecting Template
#     success_url = '/thanks/'


#     # To add classes in the form, this is using get form method
    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'mypass'})
    #     return form



# This code is to add classes to form through forms.py 
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'




class StudentTemplateView(TemplateView):
    template_name = 'school/thanks.html'

# for form class get form method
# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name','email','password']
#     success_url = '/updated/'

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'mypass'})
    #     return form

# This code is to add classes to form through forms.py 
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/updated/'



class StudentUpdateTemplateView(TemplateView):
    template_name = 'school/updated.html'
