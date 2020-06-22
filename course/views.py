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




def chapter_list(request, courseid):
    #print(coursename)
    #print(Course.objects.filter(pk=courseid).first())
    context = {
        'chapters':Chapter.objects.filter(name_of_course_id=courseid),
        'coursename':Course.objects.filter(pk=courseid).first(),
    }
    return render(request, 'course/chapterlist.html', context)


def topic_list(request, chapterid):

    coursename = Course.objects.filter(chapter__pk=chapterid).first()
    chaptername = Chapter.objects.filter(pk=chapterid).first()
    context = {
        'topics': Topic.objects.filter(chapter__pk=chapterid).all(),
        'chapterlist':Chapter.objects.filter(name_of_course=coursename),
        'coursename' : coursename, 
        'chaptername' : chaptername,
    }
    return render(request, 'course/topic_list.html', context)


def topic_single(request, topicid):

    chaptername = Chapter.objects.filter(topic__pk=topicid).first()
    coursename = Course.objects.filter(chapter__name_of_chapter=chaptername).first()
    topicname = Topic.objects.filter(pk=topicid).first()
    # print(Topic.objects.filter(chapter=chaptername))

    context = {

        'topics' : Tutorial.objects.filter(name_of_topic__pk=topicid),
        'topiclist' : Topic.objects.filter(chapter=chaptername),
        'topicname' : topicname,
        'coursename': coursename,
        'chaptername': chaptername,


    }
    #print(Course.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().course_name_id).first().name)
    #ch=Chapter.objects.filter(id=Topic.objects.filter(name_of_to'pic=topicname).first().chapter_id).first()
    #print(Topic.objects.filter(chapter__name_of_chapter=ch))
        # chaptername = Chapter.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().chapter_id).first()
        # #print(Course.objects.filter(id=Chapter.objects.filter(name_of_chapter=chaptername).first().name_of_course_id).first(), chaptername, "helllllllllllll")
        # #print(Topic.objects.filter(chapter__name_of_chapter=Chapter.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().chapter_id).first()))
        # context = {

        #     'topics': Tutorial.objects.filter(name_of_topic__name_of_topic=topicname),
        #     'topicname' : topicname,
        #     'chaptername' : Chapter.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().chapter_id).first(),
        #     'coursename' : Course.objects.filter(id=Chapter.objects.filter(name_of_chapter=chaptername).first().name_of_course_id).first(),
        #     'topiclist' :Topic.objects.filter(chapter__name_of_chapter=Chapter.objects.filter(id=Topic.objects.filter(name_of_topic=topicname).first().chapter_id).first()), 
        # }
    #print(context['topics'])
    return render(request, 'course/tutorials.html', context)


def list(request):
    return render(request, 'course/scholarship.html')