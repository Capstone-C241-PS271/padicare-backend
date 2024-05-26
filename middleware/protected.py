from functools import wraps

from flask import request, current_app
import jwt


def protected_route(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return {'message': 'You are not authorized for access this resource'}, 401
        
        try:
            data=jwt.decode(token, current_app.config['SECRET_KEY'])


        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500
        
