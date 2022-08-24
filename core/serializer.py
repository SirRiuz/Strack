

# Libs
from http.client import OK
import json
from requests import Response
from core.models import BaseProductModel
from .sekeer import Sekeer




class BaseSerializer:

    query_dataset = None

    def serialize(
        self,
        response:Response
        ,model:BaseProductModel
    ) -> (list):
        
        serialize_data = []
        
        if response and response.status_code == OK:
            response_data = json.loads(response.text)
            dataset = Sekeer().find(response_data,self.query_dataset)
            sekeer = Sekeer()
            # keyboard_list = TextBlob(keyboard).words
            
            if not dataset:
                return serialize_data
            
            for data_item in dataset:
                
                name = sekeer.find(data_item,model.name).lower()
                
                # Score
                score = sekeer.find(data_item,model.score)
                score = score if score else 0
                score = 5 if score > 5 else score
                
                
                # Price
                original_price = sekeer.find(data_item,model.original_price)
                original_price = float(original_price.replace('.','')) if type(original_price) == str and original_price else original_price

                actual_price = sekeer.find(data_item,model.actual_price)
                actual_price = float(actual_price.replace('.','')) if type(actual_price) == str and actual_price else actual_price
                #actual_price = actual_price if type(actual_price) != list else None
                #actual_price = float(actual_price.replace('.','')) if type(actual_price) == str and actual_price else actual_price

                is_descount = bool(original_price and actual_price)
                is_descount = False if original_price == actual_price else is_descount
                

                # discount_label
                discount_label = sekeer.find(data_item,model.discount_label)
                discount_label = f'{int(discount_label)}%' if not type(discount_label) is str and discount_label  else discount_label
                
                origin = sekeer.find(data_item,model.origin)
                origin = origin.replace('->',':') if type(origin) is str else origin
                
                preview = sekeer.find(data_item,model.preview)
                preview = preview.replace('->',':') if type(preview) is str else preview
                
                

                #if True:
                #if re.findall(r"(?=(\b" + '\\b|\\b'.join(keyboard_list) + r"\b))", name.lower()):
                serialize_data.append({
                        'id':sekeer.find(data_item,model.id),
                        'actual_price':actual_price,
                        'original_price':original_price,
                        'is_descount':is_descount,
                        'discount_label':discount_label,
                        'is_free_shipping':bool(sekeer.find(data_item,model.free_shipping)),
                        'name':name,
                        'origin':origin,
                        'preview':preview,
                        'description':sekeer.find(data_item,model.description),
                        'score':score
                })
                    
        
        return serialize_data


