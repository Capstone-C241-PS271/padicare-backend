from keras import models, preprocessing
import numpy as np

def load_model(model_path):
    model = models.load_model(model_path)
    return model

def preprocess_image(image_path):
    img = preprocessing.image.load_img(image_path, target_size=(224, 224))
    x = preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    img_array = np.vstack([x])
    img_array /= 255.0

    return img_array