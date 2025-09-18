from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

# Create a router and register our viewset with it.
router = routers.DefaultRouter()
router.register(r'sendmail', ContactFormViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]