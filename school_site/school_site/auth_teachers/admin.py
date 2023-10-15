from django.contrib import admin

from school_site.auth_teachers.models import AppUser


# Register your models here.


@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    pass
