



# Settings
from providers.olx.serializer import OlxSerializer
from .settings import PROVIDER_URL


# Libs
from core.provider import BaseProvider



class Olx(BaseProvider):
        
    def __init__(self,**kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)
        
        

