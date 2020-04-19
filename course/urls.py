from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from course import views

urlpatterns = [
    path('hsc/', views.course_list_hsc, name = 'courseListHsc' ),
    path('ssc/', views.course_list_ssc, name = 'courseListSsc' ),
    path('course-single/', views.course_single, name = 'courseSingle' ),
]
