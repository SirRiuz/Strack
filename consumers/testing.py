


# libs
from core.consumer import BaseConsumer
from providers.amazon.provider import Amazon


# Providers
from providers.linio.provider import Linio
from providers.olimpica.provider import Olimpica
from providers.olx.provider import Olx
from providers.movistar.provider import Movistar
from providers.falabella.provider import Falabella
from providers.mac_center.provider import MacCenter
from providers.shopee.provider import Shopee
from providers.tradeinn.provider import Tradeinn
from providers.exito.provider import Exito
from providers.mercadolibre.provider import MercadoLibre
from providers.linio.provider import Linio


class TestConsumer(BaseConsumer):
    
    provider_list = [
        Amazon,
        Olimpica,
        Shopee,
        Movistar,
        #Tradeinn,  <- Obsoleto
        Olx,
        MacCenter,
        #Exito <- Obsoleto
        Falabella,
        MercadoLibre,
        Linio
    ]


