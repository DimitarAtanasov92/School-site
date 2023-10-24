from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _

from school_site.students.models import Student
from school_site.subject.models import Teacher, UserModel


class RegisterUserForm(auth_forms.UserCreationForm):

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password!!!"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.help_text = _("It works")

    def save(self, commit=True):
        user = super().save(commit)

        profile = Teacher(email=self.cleaned_data["email"],
                          user=user, first_name=self.cleaned_data["first_name"],
                          last_name=self.cleaned_data["last_name"])
        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ("email", "first_name", "last_name", "is_teacher")


class RegisterUserFormStudent(auth_forms.UserCreationForm):

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password!!!"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.help_text = _("It works")

    def save(self, commit=True):
        user = super().save(commit)

        profile = Student(email=self.cleaned_data["email"],
                          user=user, name=self.cleaned_data["first_name"], last_name=self.cleaned_data["last_name"])
        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ("email", "first_name", "last_name", "is_student")
