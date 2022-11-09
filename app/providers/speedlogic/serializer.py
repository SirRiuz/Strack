

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.speedlogic.settings import PROVIDER_ICON



class SpeedlogicSerializer(BaseSerializer):
    
    query_dataset = '<div::aux-recent-product-item/>'
    content_type = 'html'
    #debug_response = True
        
    class model(BaseProductModel):
        name:str = '"<h2::woocommerce-loop-product__title/>".lower()'
        actual_price:float = 'float("<span::woocommerce-Price-amount amount/>".replace("$","").replace(".",""))'
        preview:str = '"<img::aux-featured-image|src/>"'
        origin:str = '"<a::woocommerce-LoopProduct-link|href/>"'
        provider_icon:str = f'"{PROVIDER_ICON}"'
