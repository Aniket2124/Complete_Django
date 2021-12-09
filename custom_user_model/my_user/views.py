from os import name
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
# Create your views here.
def home(request):
    user_model = get_user_model()
    all_user = user_model.objects.all()
    return render(request,'home.html', {'all_user':all_user})


def create_new_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        blog_title = request.POST['blog_title']
        user_model = get_user_model()
        user_obj = user_model.objects.create_user(email=email, name=name)
        user_obj.set.password(password)
        user_obj.blogpost.title = blog_title
        user_obj.save()
        return redirect('home')
    else:
        return render(request, 'create.html')