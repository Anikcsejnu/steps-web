from django.shortcuts import render
from course.models import Course
from teacher.models import TeachersInfo


# Create your views here.

def index(request):
	return render(request, 'home/index.html')


def about(request):
	context = {
		'number_of_teacher':TeachersInfo.objects.all().count(),
		'number_of_course':Course.objects.all().count(),
	}
	return render(request, 'home/about.html', context)


def courses(request):
	return render(request, 'home/courses.html')


def blog(request):
	return render(request, 'home/blog.html')