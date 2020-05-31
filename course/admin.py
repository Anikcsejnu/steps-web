from django.contrib import admin
from .models import *
# Register your models here.

class ChapterInline(admin.TabularInline):
    model = Chapter


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        ChapterInline
    ]
    class Meta:
        model = Course


admin.site.register(Course, CourseAdmin)

class TopicInline(admin.TabularInline):
    model = Topic


class ChapterAdmin(admin.ModelAdmin):
    inlines = [
        TopicInline
    ]
    
    class Meta:
        model = Chapter


admin.site.register(Chapter, ChapterAdmin)

class TutorialInline(admin.TabularInline):
    model = Tutorial
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            extra + obj.tutorial_set.count()
        return extra


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        TutorialInline
    ]

    class Meta:
        model = Topic


admin.site.register(Topic, TopicAdmin)
admin.site.register(Tutorial)