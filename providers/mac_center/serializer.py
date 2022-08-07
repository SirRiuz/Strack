



# Libs
from core.models import BaseProductModel
from providers.mac_center.settings import (PROVIDER_BASE_URL)
from core.serializer import BaseSerializer



class CenterSerailizer(BaseSerializer):
    
    query_dataset = 'items'
        
    class model(BaseProductModel):
        id:str = 'seoUrlSlugDerived'
        name:str = 'displayName'
        preview:str = f'{PROVIDER_BASE_URL} + :primaryMediumImageURL'
        origin:str = f'{PROVIDER_BASE_URL} + :route'
        original_price: float = 'childSKUs:0:listPrice'
        actual_price:float = 'childSKUs:0:salePrice'



