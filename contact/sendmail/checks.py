from django.core.checks import register, Error
from django.conf import settings


@register()
def check_basic_email_settings(app_configs, **kwargs):
    errors = []

    backend = getattr(settings, 'EMAIL_BACKEND',
                      'django.core.mail.backends.smtp.EmailBackend')
    is_smtp = 'smtp' in backend

    required_settings = [
        getattr(settings, 'EMAIL_HOST', None),
        getattr(settings, 'EMAIL_PORT', None),
        getattr(settings, 'EMAIL_HOST_USER', None),
        getattr(settings, 'EMAIL_HOST_PASSWORD', None),
        getattr(settings, 'EMAIL_RECIPIENT', None),
    ]

    use_tls = getattr(settings, 'EMAIL_USE_TLS', False)
    use_ssl = getattr(settings, 'EMAIL_USE_SSL', False)

    if is_smtp and (not all(required_settings) or not (use_tls or use_ssl)):
        errors.append(
            Error(
                'Email settings may be incomplete or misconfigured.',
                hint=(
                    'Ensure EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER,    EMAIL_HOST_PASSWORD, EMAIL_RECIPIENT and '
                    'either EMAIL_USE_TLS or EMAIL_USE_SSL are set correctly in settings.py.'
                ),
                id='gridh_contact_forms.E001',
            )
        )

    return errors
