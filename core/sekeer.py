


import json
from bs4.element import Tag
import ast



class Sekeer:    
    
    
    def __find_in_json(self,data:dict,query:str) -> (str):
        
        data = data
        query = query
        
        try:
            for q in query.split(':'):
                if q.isnumeric():
                    data = data[int(q)]
                else:
                    if data:
                        data = data.get(q)
            

            return str(data).replace('"','') if data else ''     # Error
        
        except:
            return ''
        
        
    def __freeze_text(self,text:str) -> (str):
        text = text.replace('"','')
        return text
        
        
    def __find_in_html(self,data,query:str,many:bool=False) -> (Tag):
                
        query_split_data = query.split('|')
        query_data = query_split_data[0]
        query_params = query_split_data[1].replace(' ','') if len(query_split_data) > 1 else None        
        query_split = query_data.split('::')
        tag_name = query_split[0]
        tag_class = query_split[1]


        if many:
            return data.find_all(tag_name,class_=tag_class)
        
        if query_params:
            return data.find(tag_name,class_=tag_class).get(query_params)
        
        
        return self.__freeze_text(
            data.find(tag_name,class_=tag_class).text
        ) if data.find(tag_name,class_=tag_class) else ''
      
        

    def __parse_query(self,query) -> (tuple):
        
        cap = False
        str_query = ''
        query = query
        str_query_list = []        

        for index in range(0,len(query)):
            
            if query[index] == '<':
                cap = True
        
            if query[index] == '/':
                cap = False
                str_query_list.append(
                    str_query[0:len(str_query) - 1]
                )
                str_query = ''
                
            if cap:
                str_query = str_query + query[index + 1]
                
        return tuple(str_query_list)   
    
    
    def find(self,data:dict,query:str,type_render='json',many=False) -> (str):

        try:
            if type_render == 'json':
                str_query_list = self.__parse_query(query)
                _query = query
                for query in str_query_list:
                    _query = _query.replace(
                        f'<{query}/>',
                        self.__find_in_json(
                            data=data,
                            query=query
                        )
                    )
                    
                return eval(_query)
                
                
                
            if many:
                query = self.__parse_query(query)[0]
                return self.__find_in_html(
                    data=data,
                    query=query,
                    many=True
                )


            str_query_list = self.__parse_query(query)
            _query = query
            for query in str_query_list:
                _query = _query.replace(
                    f'<{query}/>',str(self.__find_in_html(data=data,query=query))
                )

            return eval(_query)
        
        except Exception as e:
            pass

