from django.shortcuts import render
from .models import *

# Create your views here.

def events(request):
	context = {

		'events': Event.objects.all()
	}
	return render(request, 'events/events.html', context)