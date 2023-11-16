from django.shortcuts import render
from django.views import generic as views
from school_site.students.models import Student


class StudentsDetailsView(views.DetailView):
    model = Student
    template_name = "students/student_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.object
        math_grades = student.grade_set.filter(subject__name='Math')
        history_grades = student.grade_set.filter(subject__name='History')
        note = student.note_set.all()
        absence = student.absence_set.all()
        context['note'] = note
        context['absence'] = absence
        context['math_grades'] = math_grades
        context['history_grades'] = history_grades
        return context


class StudentsAddGANView(views.ListView):
    model = Student
    template_name = 'students/students.html'
    # paginate_by = 5
