from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
from teacher.models import TeachersInfo

# Register your models here.
admin.site.register(TeachersInfo)