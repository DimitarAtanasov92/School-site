from django import forms
from .models import Absence, Note, Grade


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['absences', "date"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text', "date"]


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["grade", "date", "subject"]
