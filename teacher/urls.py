from django.urls import path
from teacher import views

urlpatterns = [
	
	path('hsc/', views.teacher_hsc, name='teacher_hsc'),
	path('ssc/', views.teacher_ssc, name='teacher_ssc'),
	path('teacherdetails/<int:pk>/', views.TeacherDetialsView.as_view(), name='teacher')
]