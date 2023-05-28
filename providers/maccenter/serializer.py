# Libs
from core.models import BaseProductModel
from providers.maccenter.settings import (PROVIDER_BASE_URL)
from core.serializer import BaseSerializer

class CenterSerailizer(BaseSerializer):
    
    query_dataset = '<items/>'
        
    class model(BaseProductModel):
        name:str = '"<displayName/>".lower()'
        preview:str = f'"{PROVIDER_BASE_URL}" + "<primaryMediumImageURL/>"'
        origin:str = f'"{PROVIDER_BASE_URL}" + "<route/>"'
        original_price:float = 'float("<childSKUs:0:listPrice/>") if "<childSKUs:0:salePrice/>" else None'
        actual_price:float = 'float("<childSKUs:0:salePrice/>") if "<childSKUs:0:salePrice/>" else float("<childSKUs:0:listPrice/>")'



