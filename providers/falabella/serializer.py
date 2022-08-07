

# Libs
from core.models import BaseProductModel
from .settings import MEDIA_URL
from core.serializer import BaseSerializer



class FalabellaSerializer(BaseSerializer):
    
    query_dataset = 'data:results'
        
    class model(BaseProductModel):
        id:str = 'productId'
        name:str = 'displayName'
        origin:str = 'url'
        actual_price:float = 'prices:0:price:0'
        original_price:float = 'prices:1:price:0'
        preview:str = f'{MEDIA_URL} + media:id'




