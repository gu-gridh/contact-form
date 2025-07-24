from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    # Simple spam protection with a honeypot
    interesting = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_interesting(self):
        value = self.cleaned_data.get("interesting")
        if value:
            raise forms.ValidationError("Spam detected.")
        return value
