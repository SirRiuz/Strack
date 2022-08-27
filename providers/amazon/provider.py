



#Libs
from core.provider import BaseProvider
from providers.amazon.serializer import AmazonSerializer
#from providers.amazon.serializer import ExitoSerializer
from providers.amazon.settings import PAYLOAD_DIR, PROVIDER_URL



class Amazon(BaseProvider):
    
    serializer_class = AmazonSerializer
    
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            payload=PAYLOAD_DIR
        )



