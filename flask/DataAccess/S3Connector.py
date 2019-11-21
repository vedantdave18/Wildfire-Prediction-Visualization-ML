from boto3 import client
import joblib
import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
BUCKET_NAME = os.environ.get('BUCKET_NAME', None)
MODEL_FILE_NAME = os.environ.get('MODEL_FILE_NAME', None)
MODEL_LOCAL_PATH = '/tmp/' + MODEL_FILE_NAME

class S3Connector(object):
    # Connect to S3 Bucket
    conn = client(
        's3',
        'us-east-1',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    conn.download_file(BUCKET_NAME, MODEL_FILE_NAME, MODEL_LOCAL_PATH)
    
    # Load model from temp directory
    model = joblib.load(MODEL_LOCAL_PATH)

    # Remove serialized model to free space
    os.remove(MODEL_LOCAL_PATH)