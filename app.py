from flask import Flask
from config import config
from entity.base import db
from controller.user_urls import user_urls
from controller.post_urls import post_urls
import os

app = Flask(__name__) 
app.config.from_object(config[os.getenv("CONFIG_MODE")])

db.init_app(app)

app.register_blueprint(user_urls)
app.register_blueprint(post_urls)