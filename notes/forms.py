from django import forms
from .models import Note


class DateInput(forms.DateInput):
    input_type = 'date'


class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'due_date', 'label')
        widgets = {
            'due_date': DateInput(),
        }
