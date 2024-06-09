gcloud run deploy --project=padicare-425808 \
    --region=asia-southeast2 \
    --set-env-vars "CONFIG_MODE=production" \
    --set-env-vars "PRODUCTION_DATABASE_URL=postgresql+psycopg2://postgres:Gajahmada12@$@34.128.116.217:5432/padicare?host=/cloudsql/padicare-425808:asia-southeast2:padicare-db" \
    --set-env-vars "BUCKET_NAME=buckets-padicare" \
    --set-env-vars "JWT_SECRET_KEY=jn4cbdf.fnrffhvr" \
    --add-cloudsql-instances padicare-425808:asia-southeast2:padicare-db \
    --allow-unauthenticated