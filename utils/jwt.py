import jwt
import os
import datetime

def sign(payload):
    payload['exp'] = datetime.datetime.now() + datetime.timedelta(minutes=240)
    token = jwt.encode(payload, os.environ.get('JWT_SECRET_KEY'))
    return token

def verify(token):
    return jwt.decode(token, os.environ.get('JWT_SECRET_KEY'))