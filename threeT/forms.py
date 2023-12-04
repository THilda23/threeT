from django import forms
from .models import Choice

class ChoiceForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Choice.objects.none())
