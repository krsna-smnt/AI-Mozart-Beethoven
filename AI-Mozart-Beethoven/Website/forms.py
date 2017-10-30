from django import forms
from django.forms import ModelForm
from .models import Music


class MusicForm(forms.ModelForm):
    audio = forms.FileField(label='Music file')

    class Meta:
    	model = Music
    	fields = {'audio'}
