# libs
from core.consumer import BaseConsumer


class ElectronicConsumer(BaseConsumer):    
    provider_list = (
        'mercadolibre',
        'clonesyperifericos',
        'speedlogic',
        'olx',
        'shopee',
        'alkosto',
        'amazon',
        'linio',
        'falabella',
        'ebay'
    )
