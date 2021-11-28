from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ContactForm
from django.views.generic.edit import FormView


# Create your views here.

class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    success_url = '/thankyou/'

    # To show initial data
    initial = {'name':'Aniket'}

    #to save or print data 
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])

        return super().form_valid(form)
        # return HttpResponse('msg sent')

class ThanksTemplateView(TemplateView):
     template_name = 'school/thankyou.html'

