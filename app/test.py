
import boto3
from settings import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY
from core.storage import *

# client = boto3.client(
#     's3',
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
# )
# print(client.get_object(
#     Bucket='itrack-font',
#     Key='pol.html'
# ))

add_to_storage('this is a storage',{
    'data':'hello world'
})



