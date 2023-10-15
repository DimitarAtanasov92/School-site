from django.urls import path

from school_site.auth_teachers.views import LoginUserView, LogoutUserView, ProfileDetailView, RegisterUserView

urlpatterns = [
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("logout/", LogoutUserView.as_view(), name="logout_user"),
    path("register/", RegisterUserView.as_view(), name="register_user"),
    path("details/<int:pk>", ProfileDetailView.as_view(), name="details_user"),
]
