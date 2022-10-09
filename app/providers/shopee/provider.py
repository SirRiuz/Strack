



# Settings
from providers.shopee.serializer import ShopeeSerializer
from .settings import PROVIDER_URL


# Libs
from core.provider import BaseProvider



class Shopee(BaseProvider):
        
    serializer_class = ShopeeSerializer
        
    def __init__(self,**kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)
        
        

