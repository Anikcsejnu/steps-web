from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from course import views

urlpatterns = [
    path('hsc/', views.course_list_hsc, name = 'courseListHsc' ),
    path('ssc/', views.course_list_ssc, name = 'courseListSsc' ),
    path('chapter/<str:coursename>/', views.chapter_list, name='chapterlist'),
    path('topic/<str:chaptername>/', views.topic_list, name='topiclist'),
    path('topicsingle/<str:topicname>/', views.topic_single, name = 'topicsingle' ),
 
]
