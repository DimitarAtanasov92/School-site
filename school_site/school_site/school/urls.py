from django.urls import path

from school_site.school.views import home, events

urlpatterns = [
    path("", home, name="home"),
    path("events/", events, name="events")
]
