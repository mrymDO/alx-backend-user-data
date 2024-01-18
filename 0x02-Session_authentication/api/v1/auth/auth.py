#!/usr/bin/env python3
""" class Auth to manage the API authentication
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ class Auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        path = path.rstrip('/') + '/'
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path.rstrip('/') + '/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the request
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the request
        """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request
        """
        if request is None:
            return None

        session_name = getenv("SESSION_NAME", "_my_session_id")

        return request.cookies.get(session_name)
