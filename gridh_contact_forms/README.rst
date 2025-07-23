Contact forms for GRIDH
-----------------------

This is a small Django app for creating forms like contact forms in GRIDH's django projects.

WORK_IN_PROGRESS

gridh_contact_forms is a Django app to create simple contact forms for django projects. It has the Django REST framework as a dependency.

Quick start
-----------

1. Add "gridh_contact_forms" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "gridh_contact_forms",
    ]

2. Add "rest_framework" to your INSTALLED_APPS to be able to use the api endpoint.

3. The package uses send_mail from the Django core package. In settings also add the email configurations for your mail provider that sends the mail. You also have to add a recipient address where you want the mail to be sent to::

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.yourprovider.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your@email.com'
    EMAIL_HOST_PASSWORD = 'yourpassword'
    EMAIL_RECIPIENT = 'recipient@email.com'

4. Include the contact URLconf in your project urls.py like this::

    path("contact/", include("gridh_contact_forms.urls")),

5. Visit the ``/contact`` URL to see the contact form.

Build process
-------------

In order to build this project run python -m build in the ``gridh_contact_forms`` folder and use it in other django projects.