from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout, get_user_model,login
from django.views.generic import CreateView, FormView
# from .forms import RegistrationForm, LoginForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic.base import TemplateView

from .models import User


from .forms import LoginForm,StudentCreationForm
from django.views.generic.edit import FormView,CreateView

# Create your views here.
user = get_user_model()


# class TeacherLoginView(FormView):
#     template_name = 'accounts/login.html'
#     success_url = '/'
#     form_class = LoginForm

#     def form_valid(self, form):
#         user = form.get_user()
#         if user is not None:
#             login(self.request, user)
#         return redirect(self.success_url)


# class TeacherSignUpView(FormView):
#     form_class = RegistrationForm
#     template_name = "account/register.html"

#     # def form_invalid(self, form):
#     #     return JsonResponse({'form': form.errors}, status=200)

#     def form_valid(self, form):
#         user = form.save()
#         name = form.cleaned_data['name']
#         phone = form.cleaned_data['phone_number']
#         print('>>>> USER INFO >>>>', name, phone)
#         # teacher.objects.create(user=user, name=name, phone_number=phone)
#         messages.success(self.request, "Your account has been created successfully verify your email.")
#         return redirect('accounts:login')

# def logout_view(request):
#     logout(request)
#     return redirect(reverse('accounts:login'))

class StudentLogin(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = '/home/'
    # def post(self,request):
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         # print(name)
    #         form.save()
            
    #         return HttpResponse('Login successfully')

    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)
        return redirect(self.success_url)



class HomeTemplateView(TemplateView):
    template_name = 'accounts/home.html'
    StudentCreationForm


class SignUpCreateView(CreateView):
    model = User
    fields = ['email','password','is_student']
    template_name = 'accounts/register.html'
    success_url = '/login/'

    
    