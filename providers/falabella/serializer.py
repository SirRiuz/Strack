

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.falabella.settings import MEDIA_URL



class FalabellaSerializer(BaseSerializer):
    
    query_dataset = '<data:results/>'
        
    class model(BaseProductModel):
        name:str = '"<displayName/>".lower()'
        origin:str = '"<url/>"'
        actual_price:float = 'float("<prices:0:price:0/>".replace(".",""))'
        original_price:float = 'float("<prices:1:price:0/>".replace(".","")) if "<prices:1:price:0/>" else None'
        preview:str = f'"{MEDIA_URL}" + "<media:id/>"'
        free_shipping:bool = 'False'




