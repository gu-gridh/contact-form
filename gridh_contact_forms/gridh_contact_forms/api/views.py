from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer


class ContactAPIView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.cleaned_data['name']
            email = serializer.cleaned_data['email']
            subject = serializer.cleaned_data['subject']
            message = serializer.cleaned_data['message']
            send_mail(
                f'From {name}, Subject: {subject}',
                f'Message: {message}\n',
                email,
                [settings.EMAIL_RECIPIENT],
                fail_silently=False,
            )
            print(f"Email sent to {settings.EMAIL_RECIPIENT} from {email}")
            return Response({'message': 'Email sent successfully'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
