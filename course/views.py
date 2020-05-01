from django.shortcuts import render, get_object_or_404
from .models import Course, Chapter, Topic
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



def topic_list(request, chaptername):
    print(chaptername)
    context = {
        'topics': Topic.objects.all(),
        'chaptername': chaptername,
    }
    return render(request, 'course/topiclist.html', context)


def chapter_list(request, coursename):
    print(coursename)
    context = {
        'chapters':Chapter.objects.all(),
        'coursename':coursename,
    }
    return render(request, 'course/chapterlist.html', context)


def topic_single(request, topicname):
    print(topicname)
    context = Topic.objects.filter(name_of_topic=topicname)
    print(context[0].name_of_chapter)
    return render(request, 'course/course-single.html', { 'topic':context[0] })