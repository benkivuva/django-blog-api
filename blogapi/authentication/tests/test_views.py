from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.conf import settings
import jwt
from authentication.views import RegisterView, LoginView

# class RegisterViewTest(APITestCase):
    # def test_register_user(self):
    #    url = reverse('register')  # Generates the URL for the 'register' view

    #     # Define the user data for registration
    #     user_data = {
    #         'username': 'testuser',
    #         'password': 'testpassword',
    #         'email': 'test@example.com',
    #     }

    #     response = self.client.post(url, user_data, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #     user = User.objects.get(username='testuser')
    #     self.assertEqual(user.email, 'test@example.com')

class LoginViewTest(APITestCase):
    def test_login_user(self):
        # Create a user for testing login
        user = User.objects.create_user(username='testuser', password='testpassword')

        url = reverse('login')  # Generates the URL for the 'login' view

        # Define the login data
        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        response = self.client.post(url, login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        # Verify the JWT token
        token = response.data['token']
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(payload['username'], 'testuser')

    def test_login_with_invalid_credentials(self):
        url = reverse('login')  # Generates the URL for the 'login' view

        # Define invalid login data
        invalid_login_data = {
            'username': 'testuser',
            'password': 'invalidpassword',
        }

        response = self.client.post(url, invalid_login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)