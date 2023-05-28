

# Libs
from core.provider import BaseProvider
from providers.maccenter.serializer import CenterSerailizer
from providers.maccenter.settings import PROVIDER_URL

class Maccenter(BaseProvider):
    serializer_class = CenterSerailizer    
    def __init__(self, **kwargs):
        super().__init__(**kwargs,url=PROVIDER_URL)
