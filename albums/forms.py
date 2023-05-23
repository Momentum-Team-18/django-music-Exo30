from django import forms
from .models import Album

class Form(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name", 'artist',]
        labels = {"name": "Album Name", "artist": "Artist"}