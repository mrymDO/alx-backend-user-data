#!/usr/bin/env python3
""" BasicAuth class that inherits from Auth
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorozation header
        """
        if authorization_header is None or\
                not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        base64_part = authorization_header[len("Basic "):].strip()
        return base64_part

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode Base64 Authorization Header
        """
        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user email and password from Base64 decoded value
        """
        if decoded_base64_authorization_header is None or\
                not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)

        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if len(users) <= 0:
            return None

        user_instance = users[0]
        if not user_instance.is_valid_password(user_pwd):
            return None

        return user_instance

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the request using Basic Authentication
        """
        if request is not None:
            auth_header = self.authorization_header(request)
            base64_auth_header = self.extract_base64_authorization_header(
                    auth_header)
            decoded_auth_header = self.decode_base64_authorization_header(
                    base64_auth_header)
            user_email, user_pwd = self.extract_user_credentials(
                    decoded_auth_header)
            user = self.user_object_from_credentials(user_email, user_pwd)

            return user

        return None
