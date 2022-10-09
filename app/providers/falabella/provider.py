


# Libs
from providers.falabella.serializer import FalabellaSerializer
from providers.falabella.settings import PROVIDER_URL
from core.provider import BaseProvider



class Falabella(BaseProvider):
    
    serializer_class = FalabellaSerializer

    def __init__(self,**kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)

