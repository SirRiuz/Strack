

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.falabella.settings import MEDIA_URL, PROVIDER_ICON



class FalabellaSerializer(BaseSerializer):
    query_dataset = '<data:results/>'
    debug_response = True
        
    class model(BaseProductModel):
        name:str = '"<displayName/>".lower()'
        origin:str = '"<url/>"'
        actual_price:float = 'float("<prices:0:price:0/>".replace(".",""))'
        original_price:float = 'float("<prices:1:price:0/>".replace(".","")) if "<prices:1:price:0/>" else None'
        preview:str = f'"{MEDIA_URL}" + "<media:id/>"'
        free_shipping:bool = 'False'
        provider_icon:str = f'"{PROVIDER_ICON}"'




