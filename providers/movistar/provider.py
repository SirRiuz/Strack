# Libs
from core.provider import BaseProvider
from providers.movistar.serializer import MovistarSerializer
from providers.movistar.settings import (BODY, PAYLOAD_DIR, PROVIDER_URL)


class Movistar(BaseProvider):
    serializer_class = MovistarSerializer
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,body=BODY,url=PROVIDER_URL,
            payload=PAYLOAD_DIR,method='post')
