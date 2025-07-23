from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gridh_contact_forms'
    label = 'contact'

    def ready(self):
        import gridh_contact_forms.checks  # noqa: F401
