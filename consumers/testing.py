


# libs
from core.consumer import BaseConsumer


# Providers
from providers.linio.provider import Linio
from providers.olx.provider import Olx



class TestConsumer(BaseConsumer):
    
    provider_list = [
        Olx
    ]
