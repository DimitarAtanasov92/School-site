from django.urls import path

from school_site.students.views import StudentsDetailsView, StudentsAddGANView, StudentGradeDetailsView

urlpatterns = [
    path("details/<int:pk>/", StudentsDetailsView.as_view(), name="student_details"),
    path("studentList/", StudentsAddGANView.as_view(), name="studentList"),
    path("student_grade_details/<int:pk>", StudentGradeDetailsView.as_view(), name="student_grade_details"),
]
