#!/usr/bin/env python3
""" BasicAuth class that inherits from Auth
"""

from api.v1.auth.auth import Auth
import base64


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
