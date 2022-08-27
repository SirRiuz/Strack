

# Libs
from http.client import OK
from requests import Response
from core.models import BaseProductModel
from helpers.parsers import parse_htm, parse_json



class BaseSerializer:

    query_dataset = None
    content_type = 'json'
    debug_response = False


    def __debug_response(self,response:str):
        DEBUG_FORMAT = 'json' if self.content_type == 'json' else 'html'
        file = open(f'data.{DEBUG_FORMAT}','w').write(response)

    
    def serialize(self,response:Response,model:BaseProductModel) -> (list):
        
        serialize_data = [ ]
        
        if response and response.status_code == OK:
            
            if self.debug_response:
                self.__debug_response(response.text)
            
            if self.content_type == 'html':
                return parse_htm(
                    html_data=response.text,
                    dataset=self.query_dataset,
                    model=model,
                )
            
            return parse_json(
                json_data=response.text,
                dataset=self.query_dataset,
                model=model
            )
            
            
        return serialize_data
    
    


