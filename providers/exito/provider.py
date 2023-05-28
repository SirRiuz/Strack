#Libs
from core.provider import BaseProvider
from providers.exito.serializer import ExitoSerializer
from providers.exito.settings import PROVIDER_URL


class Exito(BaseProvider):
    serializer_class = ExitoSerializer    
    def __init__(self, **kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)



