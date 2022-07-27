


class BaseConsumer:

    provider_list = []
    
    def search(self,keyboard:str) -> (list):
        print('\n\nSearch :',keyboard)
        
        result_list = []
        provider_list = []
        
        
        for provider_class in self.provider_list:
            provider_object = provider_class(keyboard=keyboard)
            result = provider_object.get_data()
            result_list += result
            
            if len(result) > 0:
                provider_list.append(str(type(provider_object)))


        result_list = sorted(
            result_list,
            key=lambda k:k['price']
        )

        return ({
            'data':result_list,
            'providers':provider_list
        })
    
    
    
    
        