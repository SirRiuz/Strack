


# Libs
from core.models import BaseProductModel
from providers.olx.settings import ORIGIN_URL
from core.serializer import BaseSerializer



class OlxSerializer(BaseSerializer):
    
    query_dataset = '<data/>'
    debug_response = True
            
    class model(BaseProductModel):
        name:str = '"<title/>".lower()'
        preview:str = '"<images:0:url/>"'
        origin:str = f'"{ORIGIN_URL}" + "<id/>"'
        actual_price:float = '<price:value:raw/>'
        score = '<score/>'
        # description = '"<description/>"'




