from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'school/home.html')
# ----------------------------------------------------------------------

class HomeView(View):
    def get(self,request):
        return render(request,'school/home.html')


#passing Context in the class based view-----------------------------------------------------
def about(request):
    context = {'msg':'This is context in Function based View'}
    return render(request,'school/about.html',context)



class AboutClassView(View):
    def get(self,request):
        context = {'msg':'This is context in Class based View'}
        return render(request,'school/about.html',context)


#---------------------------------------------------------------------------------------------------------
#context form in class based view
def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            
            return HttpResponse('submitted Successfully')
    else:
        form = ContactForm()
    return render(request,'school/contact.html',{'form':form})



class ContactClassView(View):
    def get(self,request):
        form = ContactForm()
        return render(request,'school/contact.html',{'form':form})


    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            
            return HttpResponse('submitted Successfully')


#-------------------------------------------------------------------------------------------

def newsfunction(request,template_name):
    template_name= template_name
    context = {'info':'Reasons of World war 2'}
    return render(request,template_name,context)



class NewsClassView(View):
    template_name = ''
    def get(self,request):
        context = {'info':'Reasons of World war 2'}
        return render(request,self.template_name,context)




