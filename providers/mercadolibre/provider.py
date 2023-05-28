# Libs
from core.provider import BaseProvider
from providers.mercadolibre.serializer import MeliSerializer
from providers.mercadolibre.settings import PROVIDER_URL,PAYLOAD_DIR


class Mercadolibre(BaseProvider):
    serializer_class = MeliSerializer
    def __init__(self,**kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)
