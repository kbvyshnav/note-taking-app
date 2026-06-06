from django import forms 
from .models import Note


class NoteForm(forms.ModelForm):

    class Mets:
        model = Note

        fields = [
            'title',
            'content',
        ]