from django.contrib import admin

from school_site.subject.models import Subject, Grade


# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_filter = ["name"]


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_filter = ["date", "subject"]
