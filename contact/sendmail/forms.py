from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': '',
            'class': 'form-control'
        })
    )
    subject = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'form-control'
        })
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': '',
            'class': 'form-control',
            'rows': 5
        })
    )