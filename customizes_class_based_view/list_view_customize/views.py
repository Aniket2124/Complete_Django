from django.db.models.base import Model
from django.shortcuts import render
from .models import student
from django.views.generic.list import ListView

# Create your views here.
class StudentListView(ListView):
    model = student

    # You can specify any name to the template insted of default name
    template_name = 'list_view_customize/student.html'
     # You can specify any name to the context insted of default name
    context_object_name = 'students'

# Methods 
    def get_queryset(self):
        return student.objects.filter(course='Commerce')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fresher'] = student.objects.all().order_by('name')
        # you can add any name to context
        return context

    def get_template_names(self):
        # to get cookie
        if self.request.COOKIES['user'] == 'Aniket':
            template_name = 'list_view_customize/Aniket.html'
        
        else:
            template_name = self.template_name
        return [template_name]



