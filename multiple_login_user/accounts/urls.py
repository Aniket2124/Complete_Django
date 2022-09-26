from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
# from . views import TeacherLoginView,TeacherSignUpView,logout_view,studentLogin
from accounts import views


app_name = 'accounts'
urlpatterns = [
   
    # path('login',TeacherLoginView.as_view(),name='login'),
    # path('signup',TeacherSignUpView.as_view(),name='signup'),
    # path('logout',logout_view,name='signup'),
    path('login/',views.StudentLogin.as_view(),name='login'),
    path('home/',views.HomeTemplateView.as_view(),name='home'),
    path('signup/',views.SignUpCreateView.as_view(),name='signup'),


]
