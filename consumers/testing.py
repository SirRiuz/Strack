


# libs
from core.consumer import BaseConsumer
from providers.amazon.provider import Amazon
from providers.ebay.provider import Ebay


# Providers
from providers.linio.provider import Linio
from providers.olimpica.provider import Olimpica
from providers.olx.provider import Olx
from providers.movistar.provider import Movistar
from providers.falabella.provider import Falabella
from providers.shopee.provider import Shopee
from providers.mercadolibre.provider import MercadoLibre
from providers.linio.provider import Linio
from providers.mac_center.provider import MacCenter


class TestConsumer(BaseConsumer):
    
    provider_list = (
        Linio,
        Falabella,
        MercadoLibre,
        Olx,
        Shopee,
        Olimpica,
        #Movistar,     Obsoleto
        Amazon,
        Ebay,
        MacCenter,

    )


