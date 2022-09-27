from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list':question_list}
    return render(request,'polls/index.html',context)