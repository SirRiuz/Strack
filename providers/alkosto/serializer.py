# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.alkosto.settings import BASE_URL, ICON


class AlkostoSerializer(BaseSerializer):    
    query_dataset = '<results:0:hits/>'
    debug_response = True
    
    class model(BaseProductModel):
        name:str = '"<name_text_es/>"'
        preview:str = f'"{BASE_URL}" + "<img-820wx820h_string/>"'
        origin:str =f'"{BASE_URL}" + "<url_es_string/>"'
        original_price:float = 'float("<baseprice_cop_string/>")'
        actual_price:float = 'float("<lowestprice_double/>")'
        score:int = 'float("<averagescore_double_mv:0/>")'
        provider_icon:str = f'"{ICON}"'
