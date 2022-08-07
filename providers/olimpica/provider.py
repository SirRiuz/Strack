



# Settings
from providers.olimpica.serielizer import OLimpicaSerializer
from .settings import BODY, PAYLOAD_BIR, PROVIDER_URL


# Libs
from core.provider import BaseProvider



class Olimpica(BaseProvider):
        
    serializer_class = OLimpicaSerializer
        
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='post',
            body=BODY,
            payload=PAYLOAD_BIR
        )
        
        

