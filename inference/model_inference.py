import os
from .model import load_model, preprocess_image
import numpy as np

model = load_model(os.getenv("MODEL_PATH"))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

class_names = ['BACTERIALBLIGHT', 'BLAST', 'BROWNSPOT', 'HEALTHY', 'TUNGRO']

def predict(image_path):
    img_array = preprocess_image(image_path)
    classes = model.predict(img_array, batch_size=32)
    percented_classes = [round(value * 100, 2) for value in classes[0]]

    return class_names[np.argmax(percented_classes)]