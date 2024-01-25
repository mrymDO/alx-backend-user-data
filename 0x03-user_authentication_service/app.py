#!/usr/bin/env python3
"""Basic Flask app
"""

from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
