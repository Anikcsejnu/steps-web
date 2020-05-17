from django.urls import path
from gallery import views
urlpatterns = [
	
	path('', views.gallery, name='gallery'),
	path('<str:galleryname>', views.gallerySingle, name='gallerysingle')
]