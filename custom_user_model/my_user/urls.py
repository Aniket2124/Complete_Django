from django.urls import path
from my_user import views

urlpatterns = [
    path('', views.home,name='home'),
    path('create/',views.create_new_user,name='create' ),
]