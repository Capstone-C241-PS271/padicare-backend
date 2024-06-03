import jwt
from flask import request, jsonify
from functools import wraps
import os

def authentication_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'error': 'token is missing'}), 401
        try:
            claims = jwt.decode(token.replace('Bearer ', ''), os.getenv("JWT_SECRET_KEY"), ['HS256'])
        except Exception as error:
            print(error)
            return jsonify({'error': 'token is invalid/expired'})
        return f(claims, *args, **kwargs)
    return decorator