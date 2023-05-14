

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.clonesyperifericos.settings import PROVIDER_ICON



class ClonesyperifericosSerializer(BaseSerializer):
    
    query_dataset = '<div::content-product/>'
    content_type = 'html'
    debug_response = True
        
    class model(BaseProductModel):
        name:str = '"<h2::product-title/>".lower()'
        discount_label:str  = '"<span::onsale type-square left/>"'
        actual_price:float = 'float("<span::woocommerce-Price-amount amount/>".replace(",","").replace("$",""))'
        preview:str = '"<img::attachment-woocommerce_single|src/>"'
        origin:str = '"<a::product-content-image|href/>"'
        provider_icon:str = f'"{PROVIDER_ICON}"'