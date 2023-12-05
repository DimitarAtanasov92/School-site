from django import forms
from .models import Absence, Note


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['absences', "date"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text', "date"]
