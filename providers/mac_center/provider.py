

# Libs
from core.provider import BaseProvider
from providers.mac_center.serializer import CenterSerailizer
from providers.mac_center.settings import PROVIDER_URL



class MacCenter(BaseProvider):
    
    
    def __init__(self, **kwargs):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(**kwargs,url=PROVIDER_URL)
        

