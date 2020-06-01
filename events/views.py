from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def events(request):
	event_list = Event.objects.all().order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(event_list, 1)
	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		events = paginator.page(1)
	except EmptyPage:
		events = paginator.page(paginator.num_pages)
	context = {

		'events': events,
		'status': 'all',
		'today': datetime.date.today()

	}    
	return render(request, 'events/events.html', context)


# class EventDetialsView(DetailView):
# 	model = Event


class EventDetialsView(DetailView):
    # ...
    model = Event
    def get_context_data(self, **kwargs):
        context = super(EventDetialsView, self).get_context_data(**kwargs)
        context['all_objects'] = Event.objects.all()

        return context