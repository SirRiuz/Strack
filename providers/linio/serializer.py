

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer


class LinioSerializer(BaseSerializer):
    
    query_dataset = 'searchResult:original:products'
    
    class model(BaseProductModel):
        
        id:str = 'sku'
        name:str = 'name'
        actual_price:float = 'actualPrice'
        original_price:float = 'previousPrice'
        preview: str = 'image'
        origin: str = 'path#/mapi'
        free_shipping:bool = 'hasFreeShipping'
        score:float = 'seller:rating'
        discount_label: str = 'percentageOff'
         



