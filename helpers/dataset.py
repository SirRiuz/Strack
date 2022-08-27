

# Libs
import json
import pandas as pd



class Dataset:
        
    RANGE_OPERATOR = ':'
    
    @staticmethod
    def filter(data:list,keyboard:str,options:dict):
        
        """
           Este metodo se encarga de filtar y organizar los datos.
           
           Options:
             is_descount:True  -> Organiza los datos de mayor a menos , si is_descount es True 
             is_free_shipping:True -> Organiza los datos de mayor a menos , si is_free_shipping es True 
             range:'min_price:max_price' -> Permite filtrar los datos desde un rango de precio
             score:5 -> Permite filtrar los datos segun su nivel de puntuacion
        """
        
        #word_list = keyboard.split(' ')
        #regex = r"\b({})\b".format("|".join(x for x in word_list))
         
        #print(keyboard)       
        pandas = pd.DataFrame(data)
        #print(keyboard)
        #print(pandas['name'])
        #pandas = pandas[pandas['name'].str.contains(regex)]
        pandas = pandas.sort_values('actual_price',ascending=False)

        KEYS_LIST = tuple(options.keys())
        VALUES_LIST = tuple(options.values())
        
        for item_index in range(0,len(VALUES_LIST)):
            
            if KEYS_LIST[item_index] == 'range':
                if Dataset.RANGE_OPERATOR in VALUES_LIST[item_index]:
                    
                    """ Filter item by range price """
                    
                    range_expression = options.get('range').split(':')
                    min_range = range_expression[0]
                    max_range = range_expression[1]
                    pandas = pandas.query(
                        f'''actual_price >= {min_range}
                            and actual_price <= {max_range}'''
                    )
                    pandas = pandas.sort_values('actual_price',ascending=False)
            
            else:
                if VALUES_LIST[item_index]:
                    pandas = pandas.sort_values(KEYS_LIST[item_index],ascending=False)

        
        
        
        #return data
        return json.loads(pandas.to_json(orient='table'))['data']








