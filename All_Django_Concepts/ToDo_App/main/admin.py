
from django.contrib import admin
from .models import ToDo

# Register your models here.
# @admin.register(ToDo)
# class ToDoAdmin(admin.ModelAdmin):
#     pass
admin.site.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['added_date','text']
