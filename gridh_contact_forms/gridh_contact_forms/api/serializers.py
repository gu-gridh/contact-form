from rest_framework import serializers
from ..forms import ContactForm


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()

    # Include honeypot for spam protection
    interesting = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        form = ContactForm(data)
        if not form.is_valid():
            raise serializers.ValidationError(form.errors)
        return data
