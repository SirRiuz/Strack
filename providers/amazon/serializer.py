


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer



class AmazonSerializer(BaseSerializer):
    
    query_dataset = 's-result-item s-asin sg-col sg-col-12-of-12 s-widget-spacing-small'
    content_type = 'html'
    # debug_response = True
        
    class model(BaseProductModel):

        name:str = 'a-size-small a-color-base a-text-normal'
        origin:str = 'a-link-normal s-faceout-link a-text-normal'
        actual_price:float = 'a-price-whole'
        preview:str = 's-image'
        free_shipping:bool = 'puis-medium-weight-text a-text-bold'
        discount_label:str = 'a-price a-text-price puis-light-weight-text'




