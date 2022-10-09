

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.mercadolibre.settings import PROVIDER_ICON



class MeliSerializer(BaseSerializer):
    
    query_dataset = '<results/>'
        
    class model(BaseProductModel):
        id:str = '<id/>'
        name:str = '"<product:name/>".lower()'
        preview:str = '"<pictures:grid:retina/>"'
        actual_price:float = '<price:amount/>'
        original_price = '<price:original_price/>'
        origin:str = '"<permalink/>"'
        score:float = '<reviews:rating_average/>'
        free_shipping:bool = '"<tags:0/>" == "free_shipping"'
        discount_label:str = '"<price:discount_label:text/>"'
        provider_icon:str = f'"{PROVIDER_ICON}"'
        
        

