

class Pagination:
    
    def __init__(
        self,
        context:dict,
        min:int=0,
        max:int=0,
        data:list=[],
    ):
        self.__min = min
        self.__max = max
        self.__data = data
        self.__context = context
        
        
        
    def paginate(self) -> (dict):
        INFO = self.__get_pagination_info()
        NEXT_URL = None
        MAX_DATA = 0
        MIN_DATA = 0
        
        if INFO:
            BASE_URL = self.__context['base_url']
            QUERY = self.__context['query']
            MAX_DATA = INFO['max']
            MIN_DATA = INFO['min']
            NEXT_URL = f'{BASE_URL}api/v1/search/?q={QUERY}&min={MIN_DATA}&max={MAX_DATA}'
        
        
        return ({
            'next_url':NEXT_URL,
            'results':self.__data[MIN_DATA:MAX_DATA ]
        })
    


    
    def __get_pagination_info(self) -> (dict):
        
        MIN_NEXT = self.__max + 1
        MAX_NEXT = 0
        
        if not self.__max > len(self.__data):
            for _ in range(self.__min ,self.__max):
                MAX_NEXT = MAX_NEXT + 1
                
        else:
            return


        MAX_NEXT = MAX_NEXT + MIN_NEXT     
        
        return ({
            'min':MIN_NEXT,
            'max':MAX_NEXT
        })