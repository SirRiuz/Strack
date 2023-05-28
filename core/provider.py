# Python
import json
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

# Libs
import grequests
from core.burpeer import parse_request


class BaseProvider:
    serializer_class = None
    TIMEOUT = 5.5
    
    def __init__(self, **kwargs):
        self.__payload = kwargs.get('payload', '')
        self.__body = kwargs.get('body', '')
        self.__method = kwargs.get('method', 'get')
        self.__url = kwargs.get('url', '')
        self.__keyboard = kwargs.get('keyboard', '')
    
    def __get_search_params(self) -> (str):
        """ Get url param payload """
        return self.__url.replace(
            'query_keyboard', self.__keyboard)
    
    def __get_params(self) -> (dict):
        """ Get body params of the request """
        if not self.__body or not \
            'query_keyboard' in self.__body:
            raise("The 'body' and 'query_keyboard' param in necessary")

        return json.loads(self.__body.replace(
            'query_keyboard',
            self.__keyboard))
    
    def get_request(self) -> (grequests.AsyncRequest):
        """ Get the request object """
        header = {}
        if self.__method == 'post':
            disable_warnings(InsecureRequestWarning)
            header = parse_request(self.__payload)
            return grequests.post(
                self.__url,
                headers=header[0],
                json=self.__get_params(),
                verify=False,
                timeout=self.TIMEOUT)
            
        if self.__payload:
            header = parse_request(self.__payload)
            header = header[0]

        return grequests.get(
            self.__get_search_params(),
            headers=header,
            timeout=self.TIMEOUT)

    def __str__(self) -> (str):
        return f"<{self.__method.upper()} \
            '{self.__url[0:int(len(self.__url)/4)]}...'>"
