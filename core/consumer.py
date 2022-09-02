


# Libs
import grequests
from gevent import monkey as curious_george
from settings import DEBUG
from .storage import add_to_storage, get_to_storage
from helpers.dataset import Dataset
from helpers.serielizer import get_serialize_data




class BaseConsumer:
    
    def search(self,keyboard:str,options:object=None) -> (list):
        
        curious_george.patch_all(thread=False, select=False)
        req_list = []
        response_list = []
        
        products_data = []
        providers_list = []
        is_cache = False
        
        if not get_to_storage(keyboard):
            for provider_class in self.provider_list:
                prov_object = provider_class(keyboard=keyboard)
                req_list.append(prov_object.get_request())
                
                
            response_list = grequests.map(req_list)
            data = get_serialize_data(
                response_list,
                keyboard,
                self.provider_list
            )
            
            products_data = data['data']
            providers_list = data['providers']
            
            if not DEBUG:
                add_to_storage(keyboard,data)
        
        else:
            storage_data = get_to_storage(keyboard)
            products_data = storage_data['data']
            providers_list = storage_data['providers']
            is_cache = True
       
        
        return ({
            'data':Dataset.filter(
                data=products_data,
                options=options,
                keyboard=keyboard
            ),
            'providers':providers_list,
            'is_cache':is_cache,
            'query':keyboard.replace(' ','+')
        })
        


