from django.urls import path
from main import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add_todo/',views.add_todo,name='add_todo'),
]
