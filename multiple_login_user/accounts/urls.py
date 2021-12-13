from django.urls import path
from django.contrib.auth import views as auth_views
from . views import TeacherLoginView,TeacherSignUpView,logout_view


app_name = 'accounts'
urlpatterns = [
   
    path('login',TeacherLoginView.as_view(),name='login'),
    path('signup',TeacherSignUpView.as_view(),name='signup'),
    path('logout',logout_view,name='signup'),


]
