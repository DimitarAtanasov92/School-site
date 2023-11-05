from django.urls import path

from school_site.students.views import StudentsDetailsView

urlpatterns = [
    path("details/<int:pk>/", StudentsDetailsView.as_view(), name="student_details")
]