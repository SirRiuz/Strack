#Libs
from core.provider import BaseProvider
from providers.alkosto.serializer import AlkostoSerializer
from providers.alkosto.settings import (
    PROVIDER_URL,
    PAYLOAD_DIR,
    BODY
)


class Alkosto(BaseProvider):
    serializer_class = AlkostoSerializer    
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            method="post",
            payload=PAYLOAD_DIR,
            body=BODY,
            url=PROVIDER_URL)
