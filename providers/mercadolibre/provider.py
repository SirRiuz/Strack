


# Libs
from core.provider import BaseProvider
from providers.mercadolibre.serializer import MeliSerializer
from .settings import PROVIDER_URL,PAYLOAD_DIR



class MercadoLibre(BaseProvider):
    

    def __init__(self,**kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)


    
    
    
    