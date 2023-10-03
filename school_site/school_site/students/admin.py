from django.contrib import admin

from school_site.students.models import Note, Absence, Student, Teacher


# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ["date"]


@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_filter = ["date"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = ["name"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_filter = ["first_name"]
