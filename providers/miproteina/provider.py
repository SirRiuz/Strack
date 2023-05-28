# Settings
from providers.miproteina.serielizer import MiproteinaSerializer
from providers.miproteina.settings import (BODY, PAYLOAD_BIR, PROVIDER_URL)

# Libs
from core.provider import BaseProvider


class Miproteina(BaseProvider):
    serializer_class = MiproteinaSerializer        
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='post',
            body=BODY,
            payload=PAYLOAD_BIR)

