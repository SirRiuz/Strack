



#Libs
from core.provider import BaseProvider
from providers.exito.settings import PROVIDER_URL



class Exito(BaseProvider):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)



