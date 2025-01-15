from django import forms 

from .models import callback

class callbackForm(forms.ModelForm):
    class Meta:
        model=callback
        fields='__all__'

