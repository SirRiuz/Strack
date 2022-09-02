

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer



class EbaySerializer(BaseSerializer):
    
    query_dataset = '<li::s-item s-item__pl-on-bottom s-item--watch-at-corner/>'
    content_type = 'html'
    debug_response = True
    
    class model(BaseProductModel):
        
        name:str = '"<div::s-item__title/>".lower()'
        actual_price:float = 'float("<span::s-item__price/>".replace(" ","").replace("COP $",""))'
        original_price:float = 'float("<span::STRIKETHROUGH/>".replace(" ","").replace("COP $","")) if "<span::STRIKETHROUGH/>" else None'
        preview:str = '"<img::s-item__image-img|src/>"'
        origin:float = '"<a::s-item__link|href/>"'
        free_shipping:bool = 'None'
        score:float = 'None'
        discount_label:str = 'None'




