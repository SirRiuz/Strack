


from storage import add_to_storage


class BaseConsumer:

    
    def search(self,keyboard:str,cache:list=None,filter:object=None) -> (list):
        
        result_list = []
        provider_list = []
                
        if not cache:
        
            for provider_class in self.provider_list:
                provider_object = provider_class(keyboard=keyboard)
                result = provider_object.get_data()
                result_list += result
                
                if len(result) > 0:
                    provider_list.append(str(type(provider_object)))
                
            add_to_storage(keyboard,{
                'data':result_list,
                'providers':provider_list
            })
            
        else:
            result_list = cache['data']
            provider_list = cache['providers']
            

        
        
        if filter.get('range'):
            
            """
              Permite firtrar productos dependiendo de su
              precio
            """
            
            if ':' in filter['range']:
                filter_list = []
                range_split = filter['range'].split(':')
                MIN_RANGE = int(range_split[0])
                MAX_RANGE = int(range_split[1])
                
                for item in result_list:
                    if item['price'] >= MIN_RANGE and item['price'] <= MAX_RANGE:
                        filter_list.append(item)

                result_list = filter_list
                filter_list = None
                
        
        
        if filter.get('score'):
            
            """
              Permite firtrar productos dependiendo de su 
              puntuacion por estrellas
            """
            
            score = float(filter['score'])
            score = 5 if score > 5 else score
            filter_list = []
            
            for item in result_list:
                if item['score'] == score:
                    filter_list.append(item)
                    
            result_list = filter_list
            filter_list = None            

        

        result_list = sorted(
            result_list,
            key=lambda k:k['price'],
            reverse=True
        )

        return ({ 'data':result_list, 'providers':provider_list })
    
    
    
    
        