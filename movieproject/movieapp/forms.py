from django import forms
from . models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields =['name','disc','year','img']