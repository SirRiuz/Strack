# Python
from http.client import OK
from requests import Response

# Libs
from core.models import BaseProductModel
from helpers.parsers import parse_htm, parse_json


class BaseSerializer:
    query_dataset = None
    debug_response = False
    content_type = 'json'

    def serialize(self, response:Response,
                 model:BaseProductModel) -> (list):
        """ Serialize the data to python object """
        serialize_data = []
        
        if (response and response.status_code == OK):
            if self.content_type == 'html':
                return parse_htm(
                    html_data=response.text,
                    dataset=self.query_dataset,
                    model=model)
            
            return parse_json(
                json_data=response.text,
                dataset=self.query_dataset,
                model=model)
            
        return serialize_data
