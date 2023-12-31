"""
URL configuration for school_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("school_site.school.urls")),
    path("school_class/", include("school_site.school_class.urls")),
    path("students/", include("school_site.students.urls")),
    path("subject/", include("school_site.subject.urls")),
    path("auth_teachers/", include("school_site.auth_teachers.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
