from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Topic)

@admin.register(Tutorial)

class TutorialAdmin(admin.ModelAdmin):
    list_display = ['name_of_topic', 'chapter', 'name_of_teacher', 'course_name']
    search_fields = ['name_of_topic', 'course_name']
    
    class Media:

        #this path may be any you want, 
        #just put it in your static folde
        js = ("course/js/placeholder.js",)