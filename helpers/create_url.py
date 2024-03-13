from google.cloud import storage
import datetime

def upload_and_get_temporary_url(bucket_name, blob_name, pdf_content, expiration_minutes=5):
    # Configura el cliente de Storage
    client = storage.Client()

    # Selecciona el bucket
    bucket = client.bucket(bucket_name)

    # Selecciona el objeto Blob
    blob = bucket.blob(blob_name)

    # Sube el archivo PDF al bucket
    blob.upload_from_string(pdf_content, content_type='application/pdf')

    # Genera la URL temporalmente firmada
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
    temporary_url = blob.generate_signed_url(
        version='v4',
        expiration=expiration_time,
        method='GET'
    )

    return temporary_url