import os
from .model import load_model, preprocess_image
import numpy as np

model = load_model(os.getenv("MODEL_PATH"))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

class_names = ['BACTERIALBLIGHT', 'BLAST', 'BROWNSPOT', 'HEALTHY', 'TUNGRO']

recommendations = {
    'BACTERIALBLIGHT': (
        "1. Gunakan varietas padi yang tahan terhadap penyakit hawar bakteri.\n"
        "2. Terapkan sanitasi lahan yang baik, dengan membersihkan sisa-sisa tanaman yang terinfeksi.\n"
        "3. Jaga jarak tanam yang optimal untuk sirkulasi udara yang baik.\n"
        "4. Hindari pemupukan nitrogen yang berlebihan karena dapat memperparah infeksi.\n"
        "5. Gunakan pestisida berbasis tembaga jika perlu, sesuai anjuran."
    ),
    'BLAST': (
        "1. Gunakan varietas padi yang tahan terhadap penyakit blast.\n"
        "2. Terapkan rotasi tanaman dengan tanaman non-padi untuk mengurangi sumber infeksi.\n"
        "3. Jaga kebersihan lahan dan buang tanaman yang terinfeksi segera.\n"
        "4. Gunakan fungisida yang sesuai jika serangan sudah parah, sesuai anjuran.\n"
        "5. Kurangi kelembapan dengan mengatur irigasi secara tepat."
    ),
    'BROWNSPOT': (
        "1. Gunakan varietas padi yang tahan terhadap penyakit bercak coklat.\n"
        "2. Pastikan pemberian pupuk yang seimbang, terutama kalium, untuk meningkatkan ketahanan tanaman.\n"
        "3. Hindari kekeringan dan stress air pada tanaman.\n"
        "4. Gunakan fungisida jika serangan bercak coklat sudah parah, sesuai anjuran.\n"
        "5. Lakukan pengelolaan air yang baik untuk mencegah kondisi lembab berlebih."
    ),
    'TUNGRO': (
        "1. Gunakan varietas padi yang tahan terhadap virus tungro.\n"
        "2. Kendalikan vektor (wereng hijau) dengan insektisida yang sesuai.\n"
        "3. Terapkan sanitasi lahan dengan baik dan buang tanaman yang terinfeksi.\n"
        "4. Lakukan rotasi tanaman dengan tanaman non-padi untuk mengurangi sumber infeksi.\n"
        "5. Pantau populasi wereng secara rutin dan ambil tindakan pengendalian yang diperlukan."
    ),
    'HEALTHY': "Tanaman padi anda dalam kondisi sehat, tetap jaga kebersihan lahan dan lakukan pemeliharaan secara berkala."
}

def predict(image: str):
    img_array = preprocess_image(image)
    classes = model.predict(img_array, batch_size=32)
    percented_classes = [round(value * 100, 2) for value in classes[0]]

    result = class_names[np.argmax(percented_classes)]
    suggestion = recommendations[result]

    return {
        'result': result,
        'suggestion': suggestion
    }