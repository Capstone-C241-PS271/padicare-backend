import os
from flask import Flask
import psycopg2
from controller.user_controller import user_controller

app = Flask(__name__)

pg_connection_dict = {
    'dbname': os.environ.get('POSTGRES_DB'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'port': '5432',
    'host': 'localhost'
}

connection = psycopg2.connect(**pg_connection_dict)

app.register_blueprint(user_controller)