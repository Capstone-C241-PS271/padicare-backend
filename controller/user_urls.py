from flask import Blueprint, jsonify, request, current_app

from entity.base import db
from entity.user import User
from utils.jwt import sign
from bcrypt import checkpw, hashpw, gensalt
from middleware.authentication_required import authentication_required

import json

user_urls = Blueprint('user', __name__)

@user_urls.route('/')
def index():
    users = db.session.execute(db.select(User)).scalars().all()    
    users = [user.serialize() for user in users]

    return jsonify({"data": users})


@user_urls.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    username = json_data['username']
    password = json_data['password']
    # 
    user = db.session.query(User).filter(User.email == username).first()

    if user:

        if not checkpw(bytes(password, 'utf-8'), bytes(user.password, 'utf-8')):
            return current_app.response_class(
                response=json.dumps({"message": "Invalid credentials"}),
                status=401,
                mimetype='application/json'
            )

        token = sign({'id': user.id})

        return current_app.response_class(
            response=json.dumps({"token": token}),
            status=200,
            mimetype='application/json'
        )
    else:
        return current_app.response_class(
            response=json.dumps({"message": "User not found"}),
            status=404,
            mimetype='application/json'
        )
    

@user_urls.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    name = json_data['name']
    email = json_data['email']
    password = json_data['password']
    password = hashpw(bytes(password, 'utf-8'), gensalt()).decode('utf-8')

    user = db.session.query(User).filter(User.email == email).first()

    if user:
        return current_app.response_class(
            response=json.dumps({"message": "User already exists"}),
            status=400,
            mimetype='application/json'
        )

    # 
    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return current_app.response_class(
        response=json.dumps({"message": "User created"}),
        status=201,
        mimetype='application/json'
    )

@user_urls.route('/me')
@authentication_required
def me(user):
    user = db.session.query(User).filter(User.id == user['id']).first()
    return jsonify({'data': user.serialize()})