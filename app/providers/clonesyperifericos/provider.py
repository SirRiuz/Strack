


# Libs
from core.provider import BaseProvider
from providers.clonesyperifericos.serializer import ClonesyperifericosSerializer
from providers.clonesyperifericos.settings import PROVIDER_URL


class Clonesyperifericos(BaseProvider):
    
    serializer_class = ClonesyperifericosSerializer

    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL
        )

