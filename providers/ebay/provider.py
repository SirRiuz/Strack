# Libs
from core.provider import BaseProvider
from providers.ebay.serializer import EbaySerializer
from providers.ebay.settings import PAYLOAD_DIR, PROVIDER_URL


class Ebay(BaseProvider):
    serializer_class = EbaySerializer
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            payload=PAYLOAD_DIR)
