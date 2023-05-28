# Libs
import grequests
from core.models import BaseCommand
from core.mapping import Mapping
from gevent import monkey as curious_george


class ProviderList(BaseCommand):
    command = 'provider check'
    
    def run(self):
        print(f"\nCheck the state of the providers ...\n")
        ALL_PROVIDERS = len(Mapping().get_providers())
        fail = 0
        
        for provider in Mapping().get_provider_class():
            response = grequests.map([
                provider(keyboard="test")\
                    .get_request()])[0]
            
            if response and response.status_code != 200:
                fail += 1
                
            print(provider.__name__)
            print(response)
            print()
        
        print(f"\nFail providers -> {fail}/{ALL_PROVIDERS}")
