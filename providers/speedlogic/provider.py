


# Libs
from core.provider import BaseProvider
from providers.speedlogic.serializer import SpeedlogicSerializer
from providers.speedlogic.settings import PROVIDER_URL

class Speedlogic(BaseProvider):
    
    serializer_class = SpeedlogicSerializer

    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL
        )

