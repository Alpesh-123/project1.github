from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'polity', 'science_technology', 'art_culture', 'history', 'maths', 'reasoning', 'ethics', 'geography', 'literature', 'economics']
    
