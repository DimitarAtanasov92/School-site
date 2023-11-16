from django.shortcuts import render

from school_site.school.models import Event


# Create your views here.


def home(request):
    return render(request, 'school/home.html')


def events(request):

    school_events = Event.objects.all()
    context = {
        "events": school_events,
    }
    return render(request, 'school/events.html', context=context)
