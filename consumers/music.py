

# libs
from core.consumer import BaseConsumer


# Providers
from providers.mercadolibre.provider import MercadoLibre
from providers.linio.provider import Linio
from providers.olx.provider import Olx
from providers.falabella.provider import Falabella




class MusicConsumer(BaseConsumer):
    
    provider_list = [
        Linio,
        MercadoLibre,
        Falabella,
        Olx
    ]