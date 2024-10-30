# forms_app/forms.py
from django import forms

class FormName(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Enter Your name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'forms-control', 'placeholder': 'Enter Your emial'
        })
    )
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'forms-control',
            'placeholder': 'Enter Your feedback'
        })
    )
    profile_pic = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })
    )