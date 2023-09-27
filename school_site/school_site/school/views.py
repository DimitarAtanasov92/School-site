from django.shortcuts import render

from school_site.school.models import Event


# Create your views here.


def home(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'school/home.html', context=context)
