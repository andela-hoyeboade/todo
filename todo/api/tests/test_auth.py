from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestAuth(APITestCase):

    def setUp(self):
        User.objects.create_user(username='hassan', password='hassan')

    def login(self):
        response = self.client.post(
            '/api/login', data={'username': 'hassan', 'password': 'hassan'})
        self.token = 'Token ' + response.data.get('token', '')

    def test_user_can_login(self):
        response = self.client.post(
            '/api/login', data={'username': 'hassan', 'password': 'hassan'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)

    def test_get_bucketlist(self):
        self.login()

        # Set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        response = self.client.get(
            '/api/bucketlists/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data)
