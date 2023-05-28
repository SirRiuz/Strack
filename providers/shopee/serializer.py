# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.shopee.settings import (
    MEDIA_URL,
    ORIGIN_URL,
    PROVIDER_ICON
)


class ShopeeSerializer(BaseSerializer):
    query_dataset = '<data:items_response:items/>'
    debug_response = True
        
    class model(BaseProductModel):
        id:str = 'item_basic:itemid'
        name:str = '"<item_basic:name/>".lower()'
        origin:str = f'"{ORIGIN_URL}" + "<shopid/>" + "/" + "<itemid/>"'
        preview:str = f'"{MEDIA_URL}" + "<item_basic:image/>"'
        discount_label:str = '"<item_basic:discount/>"'
        original_price:float = 'float("<item_basic:price_before_discount/>".replace("00000",""))'
        actual_price:float = 'float("<item_basic:price/>".replace("00000",""))'
        score:float = '<item_basic:item_rating:rating_star/>'
        free_shipping:bool = '<item_basic:show_free_shipping/>'
        provider_icon:str = f'"{PROVIDER_ICON}"'



