from django.shortcuts import render
from .models import course
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