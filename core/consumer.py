


# Libs
#from storage import add_to_storage
import json
import grequests
from gevent import monkey as curious_george
import time



class BaseConsumer:

    
    def search(self,keyboard:str,cache:list=None,filter:object=None) -> (list):
        inicio = time.time()
        curious_george.patch_all(thread=False, select=False)
        req_list = []
        
        for provider_class in self.provider_list:
            prov_object = provider_class(keyboard=keyboard)
            req_list.append(prov_object.get_request())
            
        response_list = grequests.map(req_list)
        print(response_list)
        
        fin = time.time()
        print(f'\n{int(fin-inicio)}s\n')

        
        