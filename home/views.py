from django.shortcuts import render
from course.models import Course
from teacher.models import TeachersInfo
import random


# Create your views here.

def index(request):
	# teachers_items = TeachersInfo.objects.all()
	# teachers_items = random.sample(list(teachers_items), 3)
	# course_items = Course.objects.all()
	# course_items = random.sample(list(course_items), 3)

	# context = {

	# 	'random_teacher_object':teachers_items, 	
	# 	'random_course_items':course_items
	# }
	
	return render(request, 'home/index.html')


def about(request):
	context = {
		'number_of_teacher':TeachersInfo.objects.all().count(),
		'number_of_course':Course.objects.all().count(),
	}
	return render(request, 'home/about.html', context)


def courses(request):
	return render(request, 'home/courses.html')