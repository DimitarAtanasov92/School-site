from django.contrib import admin

from school_site.school_class.models import SchoolClass


# Register your models here.


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name", "teacher"]
