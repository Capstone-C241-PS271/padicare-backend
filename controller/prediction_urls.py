from flask import Blueprint, jsonify, request, current_app

from entity.base import db
from entity.prediction import Prediction
from middleware.authentication_required import authentication_required

prediction_urls = Blueprint('predictions', __name__)

@prediction_urls.route('/')
@authentication_required
def index(user):
    predictions = db.session.query(Prediction).filter(Prediction.user_id == user['id']).all()
    predictions = [prediction.serialize() for prediction in predictions]

    return jsonify({"data": predictions})


@prediction_urls.post('/')
@authentication_required
def create_prediction(user):
    json_data = request.get_json()
    title = json_data['title']
    content = json_data['content']

    prediction = Prediction(user_id=user['id'], title=title, content=content)
    db.session.add(prediction)
    db.session.commit()

    return jsonify({"message": "Prediction created successfully"})
