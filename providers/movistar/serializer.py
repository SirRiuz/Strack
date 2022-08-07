


# Libs
from core.models import BaseProductModel
from .settings import ORIGIN_BASE_URL,PROVIDER_BASE_URL
from core.serializer import BaseSerializer




class MovistarSerializer(BaseSerializer):
    
    query_dataset = 'searchResult'
        
    class model(BaseProductModel):
        id:str = 'offeringId'
        name:str = 'offeringName'
        preview:str = f'{PROVIDER_BASE_URL} + :picUrl'
        origin:str = f'{ORIGIN_BASE_URL} + :offeringId'
        actual_price:float = 'monthlyFee'




