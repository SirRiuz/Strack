# Libs
from core.provider import BaseProvider

# Settings
from providers.home_center.serializer import HomeCenterSerializer
from providers.home_center.settings import *


class HomeCenter(BaseProvider):
    serializer_class = HomeCenterSerializer
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            url=PROVIDER_URL)
