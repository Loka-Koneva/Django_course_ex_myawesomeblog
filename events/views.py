from django.shortcuts import render
from .models import Event

# Create your views here.
def home_page(request):
	events = Event.objects
	return render (request, 'events/home_page.html', {'events': events})