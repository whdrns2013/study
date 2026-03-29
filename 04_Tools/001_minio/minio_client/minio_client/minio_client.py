from minio import Minio
import dotenv
import os

dotenv.load_dotenv('core/.env')

client = Minio(
    os.environ['HOST_IP'],
    access_key = os.environ['MINIO_ACCESS_KEY'],
    secret_key = os.environ['MINIO_SECRET_KEY'],
    secure = False # https
)

# 버킷 관련 작업
bucket_name = 'test-bucket'