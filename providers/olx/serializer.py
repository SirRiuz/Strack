


# Libs
from core.models import BaseProductModel
from providers.olx.settings import ORIGIN_URL
from core.serializer import BaseSerializer




class OlxSerializer(BaseSerializer):
    

    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            model=self.Model
        )
        
        
    class Model(BaseProductModel):
        id:str = 'id'
        name:str = 'title'
        preview:str = 'images:0:url'
        origin:str = f'{ORIGIN_URL} + :id'
        price:float = 'price:value:raw'
        score = 'score'
        description = 'description'




