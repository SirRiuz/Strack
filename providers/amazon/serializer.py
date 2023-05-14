


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.amazon.settings import BASE_URL, PROVIDER_ICON



class AmazonSerializer(BaseSerializer):
    
    query_dataset = '<div::s-result-item s-asin sg-col sg-col-12-of-12 s-widget-spacing-small/>'
    content_type = 'html'
    debug_response = True
        
    class model(BaseProductModel):

        name:str = '"<span::a-text-normal/>".lower()'
        original_price:float = 'None'
        discount_label: str = 'None'
        actual_price:float = 'float("<span::a-price-whole/>".replace(",","")) if "<span::a-price-whole/>" else 0.0'
        score:float = '"<i::a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom/>"[0:3] if "<i::a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom/>" else None'
        preview:str = ' "<img::s-image|src/>" '
        provider_icon:str = f'"{PROVIDER_ICON}"'
        origin:str = f'"{BASE_URL}" + "<a::a-link-normal s-faceout-link a-text-normal|href/>"'
        free_shipping:bool = 'bool("<span::puis-medium-weight-text a-text-bold/>")'
        


