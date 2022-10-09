


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.medellinfit.settings import PROVIDER_ICON



class MedellinfitSerializer(BaseSerializer):
    
    query_dataset = '<div::clearfix product-wrapper zoom/>'
    debug_response = True
    content_type = 'html'

    class model(BaseProductModel):
        name:str = '"<h3::product-name/>".lower()'
        actual_price:float = 'float("<span::woocommerce-Price-amount amount/>".replace("$",""))'
        preview:str = '"<img::attachment-woocommerce_thumbnail size-woocommerce_thumbnail|src/>"'
        origin:str = '"<a::woocommerce-LoopProduct-link woocommerce-loop-product__link|href/>"'
        provider_icon:str = f'"{PROVIDER_ICON}"'


