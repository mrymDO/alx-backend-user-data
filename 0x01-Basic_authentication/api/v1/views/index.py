#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


# task1 New endpoint for testing unauthorized error handler
@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_endpoint() -> str:
    """ GET /api/v1/unauthorized
    Raise a 401 error to trigger the unauthorized error handler
    """
    abort(401)


# task2 New endpoint for testing forbidden error handler
@app_views.route('/forbidden',  methods=['GET'], strict_slashes=False)
def forbidden_endpoint() -> str:
    """ GET /api/v1/forbidden
    Raise a 403 error for forbidden error handler
    """
    abort(403)