


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.miproteina.settings import BASE_URL, PROVIDER_ICON



class MiproteinaSerializer(BaseSerializer):
    
    query_dataset = '<hits/>'
    debug_response = True

    class model(BaseProductModel):
        name:str = '"<name/>".lower()'
        original_price:float = '"<price:original_amount/>"'
        actual_price:float = 'float("<price:amount/>")'
        origin:str = f'"{BASE_URL}" + "<url/>"'
        preview:str = '"<image/>"'
        score:float = 'float("<rating/>")'
        provider_icon:str = f'"{PROVIDER_ICON}"'
        discount_label:str = '"<price:offer:name/>"'
        


