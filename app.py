from flask import Flask
from config import config
from entity.base import db
from controller.user_urls import user_urls
from controller.post_urls import post_urls
from controller.prediction_urls import prediction_urls
import os

app = Flask(__name__) 
app.config.from_object(config[os.environ.get('CONFIG_MODE', 'production')])
db.init_app(app)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + '/padicare-425808-c532d4b386da.json'

app.register_blueprint(user_urls, url_prefix='/api/users')
app.register_blueprint(post_urls, url_prefix='/api/posts')
app.register_blueprint(prediction_urls, url_prefix='/api/predictions')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 8080))