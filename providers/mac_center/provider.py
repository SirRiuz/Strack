

# Libs
from core.provider import BaseProvider
from providers.mac_center.serializer import CenterSerailizer
from providers.mac_center.settings import PROVIDER_URL



class MacCenter(BaseProvider):

    serializer_class = CenterSerailizer
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)
        

