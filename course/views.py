from django.shortcuts import render, get_object_or_404
from .models import course, chapterlist
from django.views.generic import ListView
# Create your views here.
def course_list_hsc(request):
    context = {
        'course_list':course.objects.filter(level='HSC').order_by('name'),
        'flag':True
    }
    return render(request, 'course/courses.html', context)

def course_list_ssc(request):
    context = {
        'course_list':course.objects.filter(level='SSC').order_by('name'),
    }
    return render(request, 'course/courses.html', context)

def course_single(request):
    return render(request, 'course/course-single.html')


def chapter_list(request, coursename):
    print(coursename)
    context = {
        'chapterlist':chapterlist.objects.all(),
        'coursename':coursename,
    }
    return render(request, 'course/chapterlist.html', context)

