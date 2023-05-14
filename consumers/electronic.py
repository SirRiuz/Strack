


# libs
from core.consumer import BaseConsumer
from providers.amazon.provider import Amazon
from providers.clonesyperifericos.provider import Clonesyperifericos
from providers.ebay.provider import Ebay


# Providers
from providers.linio.provider import Linio
from providers.medellinfit.provider import Medellinfit
from providers.miproteina.provider import Miproteina
from providers.olimpica.provider import Olimpica
from providers.olx.provider import Olx
from providers.movistar.provider import Movistar
from providers.falabella.provider import Falabella
from providers.shopee.provider import Shopee
from providers.mercadolibre.provider import MercadoLibre
from providers.linio.provider import Linio
from providers.mac_center.provider import MacCenter
from providers.speedlogic.provider import Speedlogic


class ElectronicConsumer(BaseConsumer):
    
    provider_list = (
        Clonesyperifericos,
        Speedlogic,
        Amazon,
        Medellinfit,
        Miproteina,
        #Linio,
        Falabella,
        MercadoLibre,
        Olx,
        Shopee,
        Olimpica,
        # #Gtech,     #Very low
        # #Movistar,     Obsoleto
        # Ebay,           #Obsoleto
        # #MacCenter,      Obsoleto
    )


