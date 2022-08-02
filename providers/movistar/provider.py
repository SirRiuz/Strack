



# Settings
from .settings import (BODY,PAYLOAD_DIR,PROVIDER_URL)

# Libs
from core.provider import BaseProvider


# Serializer
from .serializer import MovistarSerializer




class Movistar(BaseProvider):

    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,body=BODY,url=PROVIDER_URL,
            payload=PAYLOAD_DIR,method='post'
        )






