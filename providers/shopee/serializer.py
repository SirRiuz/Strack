


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.shopee.settings import MEDIA_URL



class ShopeeSerializer(BaseSerializer):
    
    query_dataset = 'data:items_response:items'
        
    class model(BaseProductModel):
        id:str = 'item_basic:itemid'
        name:str = 'item_basic:name'
        # origin:str = 'shopid + /'
        preview:str = f'{MEDIA_URL}+:item_basic:image'
        discount_label:str = 'item_basic:discount'
        original_price:float = 'item_basic:price_before_discount#00000'
        actual_price:float = 'item_basic:price#00000'
        score:float = 'item_basic:item_rating:rating_star'
        free_shipping:bool = 'item_basic:show_free_shipping'



