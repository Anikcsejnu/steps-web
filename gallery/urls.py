from django.urls import path
from gallery import views
urlpatterns = [
	
	path('', views.gallery, name='gallery'),
	path('<int:galleryid>', views.gallerySingle, name='gallerysingle')
]