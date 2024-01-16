#!/usr/bin/env python3
""" class Auth to manage the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ class Auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the request
        """
        return None
