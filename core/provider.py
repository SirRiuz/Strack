

# Libs
import json
import grequests
from urllib3 import disable_warnings
from core.burpeer import parse_request
from urllib3.exceptions import InsecureRequestWarning



class BaseProvider:
    
    serializer_class = None
    
    def __init__(self,**kwargs):
        self.__payload = kwargs.get('payload','')
        self.__body = kwargs.get('body','')
        self.__method = kwargs.get('method','get')
        self.__url = kwargs.get('url','')
        self.__keyboard = kwargs.get('keyboard','')
    
    
    def __get_search_params(self) -> (str):
        return self.__url.replace('query_keyboard','sss')

    
    def __get_params(self) -> (dict):
        return json.loads(self.__body.replace('query_keyboard',self.__keyboard))
    
    
    def get_request(self) -> (grequests.AsyncRequest):
        
        if self.__method == 'post':
            disable_warnings(InsecureRequestWarning)
            header = parse_request(self.__payload)
            return grequests.post(
                self.__url,
                headers=header[0],
                json=self.__get_params(),
                verify=False,
                timeout=.8
            )
        

        return grequests.get(
            self.__get_search_params(),
            timeout=.8
        )
        
        

    def __str__(self) -> (str):
        return f"<{self.__method.upper()} '{self.__url[0:int(len(self.__url)/4)]}...'>"
        

