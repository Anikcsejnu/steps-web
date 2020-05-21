from django.urls import path
from blog import views
urlpatterns = [
    path('', views.blog, name='blog'),
    path('single/', views.blogsingle, name='blog_single'),
]

