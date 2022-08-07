

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer



class MeliSerializer(BaseSerializer):
    
    query_dataset = 'results'
        
    class model(BaseProductModel):
        id:str = 'id'
        name:str = 'title'
        preview:str = 'pictures:stack:retina'
        actual_price:float = 'price:amount'
        original_price = 'price:original_price'
        origin:str = 'permalink'
        score:float = 'reviews:rating_average'
        free_shipping:bool = 'tags:0'
        discount_label:str = 'price:discount_label:text'
        
        
