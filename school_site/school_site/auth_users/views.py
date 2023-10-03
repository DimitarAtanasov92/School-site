from django.shortcuts import render
from django.urls import reverse_lazy


class RegisterUserView(views.CreateView):
    template_name = "register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("register_user")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = "login.html"


class LogoutUserView(auth_views.LogoutView):
    pass