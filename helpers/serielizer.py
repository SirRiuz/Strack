

def get_serialize_data(response_data:list,keyboard:str,providers:list) -> (list):
        
    item_list = []
    provider_list = []
        
    for index in range(0,len(providers)):
        provider_class = providers[index]
        serializer_class = provider_class.serializer_class
        response_object = response_data[index]
        serializer_model = serializer_class.model
                        
        data = serializer_class().serialize(
            keyboard=keyboard,
            response=response_object,
            model=serializer_model
        )
            
        if len(data) > 0:
            provider_list.append(provider_class.__name__)
                
        item_list += data
    
    return { 'data':item_list, 'providers':provider_list }
        
     
     
     
     
     