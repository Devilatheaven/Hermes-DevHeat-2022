from django.contrib import admin
from .models import student_details,teacher_details,doubts

# Register your models here.
admin.site.register(student_details)
admin.site.register(teacher_details)
admin.site.register(doubts)