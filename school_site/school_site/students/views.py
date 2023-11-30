from django.shortcuts import render
from django.views import generic as views
from school_site.students.models import Student
from school_site.subject.models import Teacher


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


class StudentGradeDetailsView(views.DetailView):
    model = Student
    template_name = 'students/student_grade_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.object
        user = self.request.user.pk
        teacher = Teacher.objects.filter(pk=user)[0]
        subjects_1 = student.grade_set.filter(subject__name=teacher.subject.all()[0])
        subjects_2 = student.grade_set.filter(subject__name=teacher.subject.all()[1])
        context["subjects1"] = subjects_1
        context["subjects2"] = subjects_2

        return context
