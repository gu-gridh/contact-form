from django.test import TestCase, override_settings


class ContactTemplateViewTests(TestCase):
    def test_contact_template_always_available(self):
        response = self.client.get('/pages/contact.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    @override_settings(USE_HEADLESS_FRONTEND=False)
    def test_contact_view_serves_template_when_not_headless(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    @override_settings(USE_HEADLESS_FRONTEND=True)
    def test_contact_view_returns_404_when_headless(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 404)
