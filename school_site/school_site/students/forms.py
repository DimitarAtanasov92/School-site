from django import forms
from .models import Absence


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['absences', "date"]
