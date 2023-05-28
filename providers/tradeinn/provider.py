


# Settings
from providers.tradeinn.serializer import TradeinnSerializer
from providers.tradeinn.settings import (PROVIDER_URL
                       ,PAYLOAD_DIR,
                       BODY)

# Libs
from core.provider import BaseProvider


class Tradeinn(BaseProvider):
    serializer_class = TradeinnSerializer
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,body=BODY,url=PROVIDER_URL,
            payload=PAYLOAD_DIR,method='post')
