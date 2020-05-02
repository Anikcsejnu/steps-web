from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
import datetime

# Create your views here.

def events(request):
	context = {

		'events': Event.objects.all().order_by('-date'),
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