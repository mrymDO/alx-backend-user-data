#!/usr/bin/env python3
""" Session expiration authentication
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth class for a new authentication mechanism
    """

    def __init__(self):
        """ Initialize SessionExpAuth
        """
        super().__init__()

        self.session_duration = int(os.getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """ Creates a Session ID with expiration date
        """
        session_id = super().create_session(user_id)

        if session_id:
            session_dict = {
                    "user_id": user_id,
                    "created_at": datetime.now()
            }

            self.user_id_by_session_id[session_id] = session_dict

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns User ID based on Session ID with expiration check
        """
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)

        if session_dict is None:
            return None

        user_id = session_dict.get("user_id")
        created_at = session_dict.get("created_at")

        if user_id is None or created_at is None:
            return None

        if self.session_duration > 0:
            expiration_time = created_at + timedelta(seconds=self.session_duration)
            if expiration_time < datetime.now():
                return None

        return user_id
