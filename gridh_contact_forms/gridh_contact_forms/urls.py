from django.urls import path
from .api.views import ContactAPIView
from . import views

urlpatterns = [
    path('contact', views.contact_view, name='contact'),
    path('api/contact/', ContactAPIView.as_view(), name='contact_api'),
    path('pages/contact.html', views.contact_template_only_view,
         name='contact'),
]
