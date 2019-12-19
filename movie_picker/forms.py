from django import forms
from .models import Movie

class MovieForm(forms.models.ModelForm):
    class Meta:
        model = Movie
        fields = ('title',)
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a movie title',
                'class': 'form-control input-lg',
            }),
        }
