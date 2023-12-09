from django.urls import path

from school_site.students import views
from school_site.students.views import StudentsDetailsView, StudentsAddGANView, StudentGradeDetailsView, \
    ErrorSubjectView, MyNoteDetailView, MyAbsenceDetailView, MyGradeDetailView

urlpatterns = [
    path("details/<int:pk>/", StudentsDetailsView.as_view(), name="student_details"),
    path("studentList/", StudentsAddGANView.as_view(), name="studentList"),
    path("student_grade_details/<int:pk>/", StudentGradeDetailsView.as_view(), name="student_grade_details"),
    path("student_grade_details/<int:pk>/add_absence/", views.add_absence, name="student_add_absence"),
    path("student_grade_details/<int:pk>/add_note/", views.add_note, name="student_add_note"),
    path("student_grade_details/<int:pk>/add_grade/", views.add_grade, name="student_add_grade"),
    path("student_grade_details/error_subject/", ErrorSubjectView.as_view(), name="errorSubject"),
    path("my_notes/<int:pk>/", MyNoteDetailView.as_view(), name="my_notes"),
    path("my_absence/<int:pk>/", MyAbsenceDetailView.as_view(), name="my_absence"),
    path("my_grade/<int:pk>/", MyGradeDetailView.as_view(), name="my_grade"),
]
