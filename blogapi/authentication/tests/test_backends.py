import jwt
from datetime import datetime, timedelta
from django.test import TestCase
from django.http import HttpRequest
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth.models import User
from authentication.backends import JWTAuthentication


class JWTAuthenticationTest(TestCase):

    def test_authenticate_valid_token(self):
        # Create a user for testing authentication
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Generate a valid JWT token for the user
        valid_token = jwt.encode({'username': 'testuser'}, settings.JWT_SECRET_KEY, algorithm="HS256")

        request = HttpRequest()
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {valid_token}'

        auth = JWTAuthentication()
        authenticated_user, _ = auth.authenticate(request)

        self.assertEqual(authenticated_user, user)

    def test_authenticate_invalid_token(self):
        # Create an invalid token
        invalid_token = "invalid_token"

        request = HttpRequest()
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {invalid_token}'

        auth = JWTAuthentication()

        with self.assertRaises(exceptions.AuthenticationFailed):
            auth.authenticate(request)

    # def test_authenticate_expired_token(self):
    #     # Generate an expired JWT token for the user
    #     expired_time = datetime.utcnow() - timedelta(seconds=1)
    #     expired_token = jwt.encode({'username': 'testuser', 'exp': expired_time}, settings.JWT_SECRET_KEY, algorithm="HS256")

    #     request = HttpRequest()
    #     request.META['HTTP_AUTHORIZATION'] = f'Bearer {expired_token}'

    #     auth = JWTAuthentication()
    #     authenticated_user, _ = auth.authenticate(request)

    #     self.assertIsNone(authenticated_user)
