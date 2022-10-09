



# Settings
from providers.medellinfit.serielizer import MedellinfitSerializer
from .settings import PROVIDER_URL


# Libs
from core.provider import BaseProvider



class Medellinfit(BaseProvider):
        
    serializer_class = MedellinfitSerializer
        
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='get',
        )
        
        

