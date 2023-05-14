


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.olimpica.settings import ORIGIN_URL, PROVIDER_ICON



class OLimpicaSerializer(BaseSerializer):
    
    query_dataset = '<data:products/>'
    debug_response = True


    class model(BaseProductModel):
        name:str = '"<productName/>".lower()'
        original_price:float = '<priceRange:listPrice:lowPrice/>'
        actual_price:float = '<priceRange:sellingPrice:lowPrice/>'
        origin:str = f'"{ORIGIN_URL}" + "<productId/>"'
        preview:str = '"<items:0:images:0:imageUrl/>"'
        provider_icon:str = f'"{PROVIDER_ICON}"'



