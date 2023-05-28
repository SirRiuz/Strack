# Settings
from providers.shopee.serializer import ShopeeSerializer
from providers.shopee.settings import PROVIDER_URL, PAYLOAD_DIR

# Libs
from core.provider import BaseProvider


class Shopee(BaseProvider):
    serializer_class = ShopeeSerializer 
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            payload=PAYLOAD_DIR,
            url=PROVIDER_URL)
