# Libs
from core.provider import BaseProvider
from providers.olimpica.serielizer import OLimpicaSerializer
from providers.olimpica.settings import BODY, PAYLOAD_BIR, PROVIDER_URL


class Olimpica(BaseProvider):
    serializer_class = OLimpicaSerializer
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='post',
            body=BODY,
            payload=PAYLOAD_BIR)
