from django.urls import path
from .views import ContactFormViewSet

urlpatterns = [
    path('', ContactFormViewSet.as_view({'post': 'create'}), name='contact_form'),
]