from flask import Flask
from config import config
from entity.base import db
from controller.user_urls import user_urls
from controller.post_urls import post_urls
from controller.prediction_urls import prediction_urls
from inference.model_inference import predict

import os

app = Flask(__name__) 
app.config.from_object(config[os.getenv("CONFIG_MODE")])


db.init_app(app)

print("TEST FOR BACTERAILBLIGHT : ".capitalize(), predict("/home/blanks/Development/padicare-backend/BACTERAILBLIGHT.jpg"))
print("TEST FOR BLAST : ".capitalize(), predict("/home/blanks/Development/padicare-backend/BLAST.jpg"))
print("TEST FOR brownspot : ".capitalize(), predict("/home/blanks/Development/padicare-backend/brownspot.jpg"))
print("TEST FOR healthy : ".capitalize(), predict("/home/blanks/Development/padicare-backend/healty.jpg"))
print("TEST FOR tugro : ".capitalize(), predict("/home/blanks/Development/padicare-backend/TUNGRO.jpg"))


app.register_blueprint(user_urls, url_prefix='/api/users')
app.register_blueprint(post_urls, url_prefix='/api/posts')
app.register_blueprint(prediction_urls, url_prefix='/api/predictions')