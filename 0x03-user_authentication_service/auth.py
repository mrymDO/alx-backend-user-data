#!/usr/bin/env python3
""" Hash password
"""

import bcrypt

 
def _hash_password(password: str) -> bytes:
    """ Hash the input âssword using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
