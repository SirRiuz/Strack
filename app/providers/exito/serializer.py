


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer



class ExitoSerializer(BaseSerializer):
    
    query_dataset = 'queryData:0:data'
        
    class model(BaseProductModel):
        id:str = 'productId'
        name:str = 'productName'
        origin:str = 'link'        
        price:float = 'priceRange:listPrice:lowPrice'
        preview:str = 'items:0:images:0:imageUrl'


