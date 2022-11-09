

# Libs
from core.models import BaseProductModel
from core.serializer import BaseSerializer
from providers.ebay.settings import PROVIDER_ICON



class EbaySerializer(BaseSerializer):
    
    query_dataset = '<div::s-item__wrapper clearfix/>'
    content_type = 'html'
    debug_response = True
    
    class model(BaseProductModel):
        name:str = '"<a::s-item__link/>".lower()'
        origin:str = '"<a::s-item__link|href/>"'
        preview:str = '"<img::s-item__image-img|src/>"'
        actual_price:float = 'float("<span::s-item__price/>".replace("COP ","").replace("$","").replace(" ","")) if not "<span::s-item__price/>".count("a") > 0 else float("<span::s-item__price/>".split("a")[0].replace("COP ","").replace("$","").replace(" ",""))'
        provider_icon:str = f'"{PROVIDER_ICON}"'




