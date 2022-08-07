


# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer



class TradeinnSerializer(BaseSerializer):
    
    query_dataset = 'results:0:hits'
    
    class model(BaseProductModel):
        id:str = 'objectID'
        name:str = 'model:spa'
        preview:str = 'src_photo'
        origin:str = 'link_product'
        actual_price:float = 'precio_str:precio_43#COL$'




