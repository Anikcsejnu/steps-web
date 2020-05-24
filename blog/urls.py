from django.urls import path
from blog import views
urlpatterns = [
    path('', views.blog, name='blog'),
    path('postdetails/<int:pk>/', views.BlogSingleDetailView.as_view(), name='blog_single'),
    path('post/', views.post_blog, name='post_blog'),
]

