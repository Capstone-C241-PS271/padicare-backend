from flask import Blueprint, jsonify, request

from entity.base import db
from entity.prediction import Prediction
from middleware.authentication_required import authentication_required
from inference.model_inference import predict
from utils.storage import upload_to_gcs
from base64 import b64decode
import numpy as np

prediction_urls = Blueprint('predictions', __name__)

@prediction_urls.get('/')
@authentication_required
def index(user):
    print('QUERY : ', request.args.get('page'))
    predictions = db.session.query(Prediction).filter(Prediction.author_id == user['id']).all()
    predictions = [prediction.serialize() for prediction in predictions]

    return jsonify({"data": predictions})


@prediction_urls.post('/')
@authentication_required
def create_prediction(user):
    json_data = request.get_json()
    image = json_data['image']
    author = user['id']

    result = predict(image)

    # Upload image to GCS
    image = b64decode(image)
    file_name = f"prediction_{np.random.randint(10000)}.jpg"
    image_url = upload_to_gcs(file_name, image)        

    prediction = Prediction(
        author_id=author, 
        image=image_url, 
        result=result['result'], 
        suggestion=result['suggestion']
    )
    db.session.add(prediction)
    db.session.commit()

    return jsonify({
        "message": "Prediction created successfully",
        "data": prediction.serialize()
    })
