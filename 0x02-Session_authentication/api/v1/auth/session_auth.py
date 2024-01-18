#!/usr/bin/env python3
""" Session authentication
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ SessionAuth class for a new authentication mechanism
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns User ID based on Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a User instance based on a cookie value
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ Delete the user session/logout
        """
        if request is None:
            return False

        session_id: str = self.session_cookie(request)

        if session_id is None:
            return False

        user_id: str = self.user_id_for_session_id(session_id)

        if user_id is None:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
