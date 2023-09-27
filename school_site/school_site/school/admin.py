from django.contrib import admin

from school_site.school.models import Event


# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]
