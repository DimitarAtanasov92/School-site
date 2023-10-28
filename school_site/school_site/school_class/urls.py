from django.urls import path

from school_site.auth_teachers.views import MyClassDetailView

urlpatterns = [path("my_class/<int:pk>", MyClassDetailView.as_view(), name="my_class"),
               ]
