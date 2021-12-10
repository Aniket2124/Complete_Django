
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views import View


# Create your views here.
#Function Based view
def myview(request):
    return HttpResponse('<h1> Function Based view</h1>')


#Class based View
class MyView(View):
    name = 'Aniket'
    def get(self, reuest):
        # return HttpResponse('<h1> Class Based view</h1>')
        return HttpResponse(self.name)

# we can create child class of view class
class MyViewChild(MyView):
    def get(self, request):
         return HttpResponse(self.name)
