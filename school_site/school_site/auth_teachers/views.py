from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from school_site.auth_teachers.forms import RegisterUserForm
from school_site.subject.models import Teacher


# Create your views here.

class LoginUserView(auth_views.LoginView):
    template_name = "auth_teachers/login.html"


class LogoutUserView(auth_views.LogoutView):
    pass


class RegisterUserView(views.CreateView):
    template_name = "auth_teachers/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class ProfileDetailView(views.DetailView):
    model = Teacher
    template_name = 'auth_teachers/profile_details.html'
