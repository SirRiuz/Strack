


# Libs
from core.provider import BaseProvider
from providers.linio.serializer import LinioSerializer
from providers.linio.settings import PAYLOAD_DIR,BODY,PROVIDER_URL



class Linio(BaseProvider):

    serializer_class = LinioSerializer

    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            payload=PAYLOAD_DIR,
            url=PROVIDER_URL,
            method='post',
            body=BODY
        )

  
  
  