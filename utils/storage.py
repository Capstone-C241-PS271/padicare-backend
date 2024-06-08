import os
from google.cloud import storage

def upload_to_gcs(file_name, file_data):
    client = storage.Client()
    bucket = client.get_bucket(os.environ.get('BUCKET_NAME'))
    blob = bucket.blob(file_name)
    blob.upload_from_string(file_data, content_type='image/jpeg')

    return blob.public_url
