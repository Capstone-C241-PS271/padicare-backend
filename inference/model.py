from keras import models, preprocessing
import numpy as np
import base64
from io import BytesIO
from PIL import Image

def load_model(model_path):
    model = models.load_model(model_path, compile=False)
    return model

def preprocess_image(image: str):
    if len(image) > 400:
        image_data = base64.b64decode(image)
        image_io = Image.open(BytesIO(image_data)).convert('RGB')
        img = image_io.resize((224, 224), Image.Resampling.LANCZOS)
    else:
        img = preprocessing.image.load_img(image, target_size=(224, 224))

    x = preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    img_array = np.vstack([x])
    img_array /= 255.0

    return img_array