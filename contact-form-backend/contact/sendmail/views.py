
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm  # Import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status

def sendmail(request):
    if request.method == 'GET':
        form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.data)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(f"Received message from {name} ({email}): {message}")
            print(f"Sending email to {settings.EMAIL_HOST_USER} from {email}")
            print(f"Sending email to {settings.EMAIL_HOST_PASSWORD} from {email}")
            send_mail(
                f'From {name}, Subject: {subject}',
                f'Message: {message}\n',
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print(f"Email sent to {settings.EMAIL_HOST_USER} from {email}")

            return HttpResponseRedirect('/success/')
    return HttpResponse('Invalid form submission', status=status.HTTP_400_BAD_REQUEST)


def success(request):
    return HttpResponse('Thank you for your message! We will get back to you soon.')