#!/usr/bin/env python3
"""Basic Flask app
"""

from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)

AUTH = Auth()


@app.route("/")
def welcome():
    """return a JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """register user
    """
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@app.route("/sessions", methods=["POST"])
def login() -> str:
    """login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout() -> str:
    """logout and redirect to GET/
    """
    session_id = request.cookies.get('session_d')

    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            AUTH.destroy_session(user.id)
            response = redirect(url_for('index'))
            response.delete_cookie('session_id')
            return response
        else:
            abort(403)
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
