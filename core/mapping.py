# Python
import os
import inspect

# Libs
from settings import PROVIDERS_DIR
from core.provider import BaseProvider


class Mapping:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super()\
                .__new__(cls, *args, **kwargs)
            
        return cls._instance
    
    def get_providers(self) -> (list):
        """
        Get a list of the all prividers
        in the 'provider' dir
        """
        providers_list = os.listdir(PROVIDERS_DIR)
        return providers_list
    
    
    def get_provider_class(self, providers=None) -> (list):
        """ Get class of the all providers """
        providers_list = []
        providers_data = self.get_providers()
        
        if providers:
            providers_data.clear()
            ALL_PROVIDERS = self.get_providers()
            for item in providers:
                if not item in ALL_PROVIDERS:
                    raise Exception(f"The provider '{item}' " \
                        + "not installed.")
                    
                providers_data.append(item)
        
        for provider in providers_data:
            provider_loader = f"{PROVIDERS_DIR}{provider}/provider.py"
            
            if not os.path.exists(provider_loader):
                raise Exception(f"The proficer '{provider}' are " \
                    + "not configurated.")
            
            data = open(provider_loader, "r").read()
            namespace = ({'__name__': '__main__'})
            exec(data, namespace)
            
            for n , item in namespace.items():
                if inspect.isclass(item) and \
                    issubclass(item, BaseProvider) and \
                        item != BaseProvider:
                            
                    providers_list.append(item)
                    
        return providers_list
