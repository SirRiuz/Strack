

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.linio.settings import ORIGIN_URL


class LinioSerializer(BaseSerializer):
    
    query_dataset = '<searchResult:original:products/>'
    debug_response = True
    
    class model(BaseProductModel):
        
        name:str = '"<name/>".lower()'
        free_shipping:bool = '"<hasFreeShipping/>"'
        discount_label: str = 'str(int(<percentageOff/>)) + "%"'
        actual_price:float = 'float(<actualPrice/>)'
        original_price:float = 'float("<previousPrice/>")'
        score:float = '<seller:rating/>'
        preview: str = '"<image/>"'
        origin: str = f'"{ORIGIN_URL}" + "/<path/>".replace("/mapi/","")'





