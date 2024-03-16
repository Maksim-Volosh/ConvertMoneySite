from django import forms
from .pars import get_curr

class CurrencyForm(forms.Form):
    curr = forms.DecimalField(label=None, max_digits=30, required=True, widget=forms.TextInput(attrs={'class': "form-control", 'id': "name-form02-6", 'placeholder': "Amount" }))
    
    CHOICES = get_curr()
    from_curr = forms.ChoiceField(label=None, choices=CHOICES, required=True, widget=forms.Select(attrs={'class': "form-control select", 'id': "textarea-form02-6"}))
    
    CHOICES_2 = get_curr()
    to_curr = forms.ChoiceField(label=None, choices=CHOICES_2, required=True, widget=forms.Select(attrs={'class': "form-control select", 'id': "textarea-form02-6"}))
