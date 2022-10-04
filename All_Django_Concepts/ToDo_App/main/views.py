from django.shortcuts import render
from django.utils import timezone
from main.models import ToDo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_objects = ToDo.objects.all().order_by("-added_date")
    return render(request,'main/index.html',{'todo_objects':todo_objects})

def add_todo(request): 
    current_date = timezone.now()
    abc = request.POST["abc"]
    data = ToDo.objects.create(added_date=current_date,text=abc)
    data.save()
    return HttpResponseRedirect("/")
