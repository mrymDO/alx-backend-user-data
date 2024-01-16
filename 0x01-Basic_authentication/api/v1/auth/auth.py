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
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip('/') == excluded_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the request
        """
        return None
