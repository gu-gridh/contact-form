from django.core import mail
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class ContactAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/contact/'

    # Beware this actually sends an email if you test this in production. Choose EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend' for your development settings and test in development.
    def test_valid_post_returns_200(self):
        payload = {
            'name': 'GRIDH',
            'email': 'gridh@example.com',
            'subject': 'testing',
            'message': 'Test message'
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)

    def test_invalid_post_returns_400(self):
        payload = {
            'name': '',
            'email': 'bad-email',
            'subject': 'testing',
            'message': ''
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_email_sent(self):
        response = self.client.post('/api/contact/', {
            'name': 'GRIDH',
            'email': 'gridh@example.com',
            'subject': 'testing',
            'message': 'Hi there',
        }, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Hi there', mail.outbox[0].body)
