Contact forms for GRIDH
-----------------------

This is a small Django app for creating forms like contact forms in GRIDH's django projects.

WORK_IN_PROGRESS

gridh_contact_forms is a Django app to create simple contact forms for django projects. It has the Django REST framework as a dependency.
If you use the templates, it currently works best together with gridh_pages. If you don't want to use those you can just overwrite the template file gridh_contact_forms/contact_form.html and use it with your own templates instead.

Quick start
-----------

1. Add "gridh_contact_forms" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "gridh_contact_forms",
    ]

2. Add "rest_framework" to your INSTALLED_APPS to be able to use the api endpoint. Also add "corsheaders" and the corresponding middleware "corsheaders.middleware.CorsMiddleware" to your project when you have a headless frontend on another server. Define CORS_ALLOWED_ORIGINS for your server for production environments.

3. The package let's you decide if you want to go headless with frameworks like Vue or use a simple version with templates. For this you need to add the following setting depending on which one you choose::
    
    USE_HEADLESS_FRONTEND = True

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