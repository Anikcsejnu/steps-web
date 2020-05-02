from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView
# Create your views here.
def course_list_hsc(request):
    context = {
        'course_list':Course.objects.filter(level='HSC').order_by('name'),
        'flag':True
    }
    return render(request, 'course/courses.html', context)

def course_list_ssc(request):
    context = {
        'course_list':Course.objects.filter(level='SSC').order_by('name'),
    }
    return render(request, 'course/courses.html', context)






def chapter_list(request, coursename):
    print(coursename)
    context = {
        'chapters':Chapter.objects.filter(name_of_course__name=coursename),
        'coursename':coursename,
    }
    return render(request, 'course/chapterlist.html', context)


def topic_list(request, chaptername):
    print(chaptername)
    context = {
        'topics': Topic.objects.filter(chapter__name_of_chapter=chaptername),
        'chaptername': chaptername,
    }
    return render(request, 'course/topiclist.html', context)


def topic_single(request, topicname):
    print(topicname)
    context = {

        'topics': Tutorial.objects.filter(name_of_topic__name_of_topic=topicname),
        'topicname' : topicname

    }
    print(context['topics'])
    return render(request, 'course/course-single.html', context)