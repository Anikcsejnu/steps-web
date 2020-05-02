from django.urls import path
from events import views


urlpatterns = [

	path('', views.events, name='events'),
	path('eventdetails/<int:pk>/', views.EventDetialsView.as_view(), name='eventdetails')

]