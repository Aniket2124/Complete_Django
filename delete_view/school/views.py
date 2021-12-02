from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Student
from django.views.generic.base import TemplateView

from.forms import StudentForm

# This code is to add classes to form through forms.py 
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'


class StudentTemplateView(TemplateView):
    template_name = 'school/thanks.html'



# This code is to add classes to form through forms.py 
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/updated/'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/deleted/'


class StudentUpdateTemplateView(TemplateView):
    template_name = 'school/updated.html'

class StudentDeleteTemplateView(TemplateView):
    template_name = 'school/deleted.html'

