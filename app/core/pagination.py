

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
        pagInfo = self.__get_pagination_info()

        min = pagInfo['min']
        max = pagInfo['max']

        BASE_URL = self.__context['base_url']
        QUERY = self.__context['query']
        MIN_DATA = pagInfo['next']['min']
        MAX_DATA = pagInfo['next']['max']
        NEXT = f'{BASE_URL}api/v1/search/?q={QUERY}&min={MIN_DATA}&max={MAX_DATA}'

        if MIN_DATA > len(self.__data):
            NEXT = None

    
        return ({
            'next':NEXT,
            'data':self.__data[min:max]
        })

    
    def __get_pagination_info(self) -> (dict):
        return ({
            'min':self.__min,
            'max':self.__max,
            'next':{
                'min':self.__max + 1,
                'max':self.__max + ( self.__max - self.__min )
            }
        })
