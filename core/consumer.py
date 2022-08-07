


# Libs
import json
import grequests
from gevent import monkey as curious_george
import time



class BaseConsumer:


    def __serialize_data(self,response_data:list,keyboard:str) -> (list):
        
        
        item_list = []
        provider_list = []
        
        for index in range(0,len(self.provider_list)):
            provider_class = self.provider_list[index]
            serializer_class = provider_class.serializer_class
            response_object = response_data[index]
            serializer_model = serializer_class.model
                        
            data = serializer_class().serialize(
                keyboard=keyboard,
                response=response_object,
                model=serializer_model
            )
            
            if len(data) > 0:
                provider_list.append(str(provider_class))
                
            item_list += data
            
        
        print(json.dumps({
            'data':item_list,
            'providers':provider_list    
        },indent=2))
            
            
            

    
    def search(self,keyboard:str,cache:list=None,filter:object=None) -> (list):
        inicio = time.time()
        curious_george.patch_all(thread=False, select=False)
        req_list = []
        
        for provider_class in self.provider_list:
            prov_object = provider_class(keyboard=keyboard)
            req_list.append(prov_object.get_request())
            
        response_list = grequests.map(req_list)
        self.__serialize_data(response_list,keyboard)
        
        fin = time.time()
        print(f'\n{int(fin-inicio)}s\n')

        
        