

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_text = form.cleaned_data['message']

            try:
                send_mail(
                    f'From {name}, Subject: {subject}',
                    f'Message: {message_text}\n\nFrom: {email}',
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                print(f"Email sent to {settings.EMAIL_HOST_USER} from {email}")
                messages.success(request, 'Your message has been sent successfully!')
                form = ContactForm()  # Clear the form
            except Exception as e:
                print(f"Error sending email: {e}")
                messages.error(request, 'Failed to send email. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'sendmail/contact_form.html', {'form': form})
