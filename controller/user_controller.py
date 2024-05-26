import json
from flask import current_app, Blueprint

user_controller = Blueprint('user_controller', __name__)


@user_controller.get('/user')
def get_user():
    return current_app.response_class(
        status=200,
        mimetype='application/json',
        response=json.dumps({'message': 'User is authenticated'}),
    )

@user_controller.post('/user')
def create_user():
    return current_app.response_class(
        status=201,
        mimetype='application/json',
        response=json.dumps({'message': 'User created'}),
    )

@user_controller.put('/user')
def update_user():
    return current_app.response_class(
        status=200,
        mimetype='application/json',
        response=json.dumps({'message': 'User updated'}),
    )

@user_controller.delete('/user') 
def delete_user():
    return current_app.response_class(
        status=200,
        mimetype='application/json',
        response=json.dumps({'message': 'User deleted'}),
    )