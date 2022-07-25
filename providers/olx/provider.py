



# Settings
from providers.olx.serializer import OlxSerializer
from .settings import PROVIDER_URL


# Libs
from core.provider import BaseProvider



class Olx(BaseProvider):
        
        
    def __init__(self,**kwargs) -> (None):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='GET'
        )


    def get_data(self) -> (dict):
        response_data = super().get_data()['data']
        data = OlxSerializer(
            data=response_data,
            keyboard=self.__keyboard
        ).serialize()
        return data


