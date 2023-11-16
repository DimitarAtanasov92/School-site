from django.urls import path

from school_site.school_class.views import MyClassDetailView

urlpatterns = [path("my_class/<int:pk>/", MyClassDetailView.as_view(), name="my_class"),
               ]
