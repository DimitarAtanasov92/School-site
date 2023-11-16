from django.shortcuts import render
from django.views import generic as views
from school_site.subject.models import Teacher


# Create your views here.


class MyClassDetailView(views.DetailView):
    model = Teacher
    template_name = "school_class/school_class.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.object
        students = teacher.schoolclass.student_set.all()
        class_name = teacher.schoolclass.name
        context['students'] = students
        context['class_name'] = class_name
        return context
