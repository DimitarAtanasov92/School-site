from django.urls import path

from school_site.school.views import home

urlpatterns = [
    path("", home, name="home"),
]
