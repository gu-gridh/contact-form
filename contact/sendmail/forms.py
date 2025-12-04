from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': '',
            'class': 'form-control'
        })
    )
    subject = forms.CharField(
        label="Subject",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'form-control'
        })
    )
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': '',
            'class': 'form-control',
            'rows': 5
        })
    )

     # Simple spam protection
    interesting = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_interesting(self):
        value = self.cleaned_data.get("interesting")
        if value:
            raise forms.ValidationError("Spam detected.")
        return value
