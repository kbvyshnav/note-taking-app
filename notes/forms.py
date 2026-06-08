from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note

        fields = [
            'title',
            'content',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Note title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your note here...',
                'rows': 8,
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')

        return title

    def clean_content(self):
        content = self.cleaned_data['content'].strip()

        if not content:
            raise forms.ValidationError('Note content cannot be empty.')

        return content