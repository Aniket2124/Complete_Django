from django.shortcuts import render
from django.contrib.auth import logout, get_user_model,login
from django.views.generic import CreateView, FormView
from .forms import RegistrationForm, LoginForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
user = get_user_model()


class TeacherLoginView(FormView):
    template_name = 'accounts/login.html'
    success_url = '/'
    form_class = LoginForm

    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)
        return redirect(self.success_url)


class TeacherSignUpView(FormView):
    form_class = RegistrationForm
    template_name = "account/register.html"

    # def form_invalid(self, form):
    #     return JsonResponse({'form': form.errors}, status=200)

    def form_valid(self, form):
        user = form.save()
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone_number']
        print('>>>> USER INFO >>>>', name, phone)
        # teacher.objects.create(user=user, name=name, phone_number=phone)
        messages.success(self.request, "Your account has been created successfully verify your email.")
        return redirect('accounts:login')

def logout_view(request):
    logout(request)
    return redirect(reverse('accounts:login'))