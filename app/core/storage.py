


# Libs
import hashlib
import json
import os
import datetime
from settings import STORAGE_DIR
import boto3
import io
from settings import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY
import redis







def add_to_storage(keyboard:str,data:dict):

    redis_client = redis.Redis(host='localhost',port='6379')
    query_hash = hashlib.sha256(keyboard.encode()).hexdigest()
    data = json.dumps(data,indent=2)

    redis_client.set(query_hash,data)
    # aws_client = boto3.client(
    #     's3',
    #     aws_access_key_id=AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    # )
    # session = boto3.Session(
    #     aws_access_key_id=AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    # )

    # s3 = session.resource("s3")

    # buff = io.BytesIO()

    # buff.write("test1\n".encode())
    # buff.write("test2\n".encode())

    # s3.Object('trak-storage', query_hash).put(Body=buff.getvalue())


