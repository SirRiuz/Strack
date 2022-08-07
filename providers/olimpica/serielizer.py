


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.olimpica.settings import ORIGIN_URL



class OLimpicaSerializer(BaseSerializer):
    
    query_dataset = 'data:products'
        
    class model(BaseProductModel):
        id:str = 'productId'
        name:str = 'productName'
        original_price:float = 'priceRange:listPrice:lowPrice'
        actual_price:float = 'priceRange:sellingPrice:lowPrice'
        origin:str = f'{ORIGIN_URL} + :productId'
        preview:str = 'items:0:images:0:imageUrl'


