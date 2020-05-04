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
    #print(Course.objects.filter(id= Chapter.objects.filter(name_of_chapter=chaptername).first().name_of_course_id ).first( ))
    context = {
        'topics': Topic.objects.filter(chapter__name_of_chapter=chaptername),
        'chaptername': chaptername,
        'coursename':Course.objects.filter(id= Chapter.objects.filter(name_of_chapter=chaptername).first().name_of_course_id ).first( ),
    }
    return render(request, 'course/topiclist.html', context)


def topic_single(request, topicname):
    #print(Course.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().course_name_id).first().name)
    #ch=Chapter.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().chapter_id).first()
    #print(Topic.objects.filter(chapter__name_of_chapter=ch))
    context = {

        'topics': Tutorial.objects.filter(name_of_topic__name_of_topic=topicname),
        'topicname' : topicname,
        'chaptername' : Chapter.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().chapter_id).first(),
        'coursename' : Course.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().course_name_id).first(),
        'topiclist' :Topic.objects.filter(chapter__name_of_chapter=Chapter.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().chapter_id).first()), 
    }
    #print(context['topics'])
    return render(request, 'course/course-single.html', context)


def list(request):
    return render(request, 'course/scholarship.html')