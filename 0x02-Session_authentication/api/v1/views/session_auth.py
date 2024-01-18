#!/usr/bin/env python3
""" Routes for Session authentication
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_session() -> str:
    """ login route
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            user_data = user.to_json()
            session_name = os.getenv('SESSION_NAME')
            response = jsonify(user_data)
            response.set_cookie(session_name, session_id)
            return response
        return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout_session() -> str:
    """ logout route
    """
    from api.v1.app import auth
    isdestroy = auth.destroy_session(request)

    if isdestroy is False:
        abort(404)

    return jsonify({}), 200
