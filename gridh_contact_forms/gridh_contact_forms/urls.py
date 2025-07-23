from django.urls import path, include
from .views import ContactFormViewSet
from rest_framework import routers

# Create a router and register our viewset with it.
router = routers.DefaultRouter()
router.register(r'', ContactFormViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
