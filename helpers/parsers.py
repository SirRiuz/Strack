

# Libs
import json
from bs4 import BeautifulSoup
from core.models import BaseProductModel
from core.sekeer import Sekeer



def parse_htm(html_data:str,dataset:str,model:BaseProductModel) -> (tuple):
    
    """ Se encarga de parcear una respuesta de tipo html """
    
    sekeer = Sekeer()    
    soup = BeautifulSoup(html_data,'html.parser')
    dataset = sekeer.find(
        data=soup,
        query=dataset,
        many=True,
        type_render='html',
    )
    data = []


    for item in dataset:
        
        score = sekeer.find(
            data=item,
            query=model.score,
            type_render='html',
            many=False
        )
                
        origin = sekeer.find(
            data=item,
            query=model.origin,
            type_render='html',
            many=False
        )
        
        origin = origin.replace('%','/') if origin else origin
        original_price = sekeer.find(
            data=item,
            query=model.original_price,
            type_render='html',
            many=False
        )
        actual_price = sekeer.find(
            data=item,
            query=model.actual_price,
            type_render='html',
            many=False
        )
        
        
        data.append({
            'name':sekeer.find(
                data=item,
                query=model.name,
                type_render='html',
                many=False
            ),
            'preview':sekeer.find(
                data=item,
                query=model.preview,
                type_render='html',
                many=False
            ),
            'origin':origin,
            'original_price':original_price,
            'actual_price':actual_price,
            'is_discount':bool(actual_price and original_price),
            'discount_label':sekeer.find(
                data=item,
                query=model.discount_label,
                type_render='html',
                many=False
            ),
            'free_shipping':sekeer.find(
                data=item,
                query=model.free_shipping,
                type_render='html',
                many=False
            ),
            'score':score
        })
    
    return data




def parse_json(json_data:str,dataset:str,model:BaseProductModel) -> (tuple):
    
    """ Se encarga de parcear una respuesta de tipo JSON """
    
    sekeer = Sekeer()
    data = []
    dataset = sekeer.find(json.loads(json_data),dataset,many=True)
        
    
    for item in (dataset if dataset else []):
                        
        # discount
        actual_price = sekeer.find(item,model.actual_price)
        original_price = sekeer.find(item,model.original_price)
        discount_label = sekeer.find(item,model.discount_label)
        #is_discount = bool(discount_label) or bool(actual_price and original_price)
        is_discount = bool(actual_price and original_price)
        
        free_shipping = bool(sekeer.find(item,model.free_shipping))
        score = sekeer.find(item,model.score)
        #score = score if score else 0
        #score = 5 if score > 5 else score
        description = sekeer.find(item,model.description)
        
        preview = sekeer.find(item,model.preview)
        name = sekeer.find(item,model.name)
        #name = name.lower() if name and type(name) is str else ''
        origin = sekeer.find(item,model.origin)
        

        data.append({
            'name':name,
            'preview':preview,
            'origin':origin,
            'actual_price':actual_price,
            'is_descount':is_discount,
            'original_price':original_price,
            'is_free_shipping':free_shipping,
            'score':score,
            'description':description,
            'discount_label':discount_label
        })
        
    
    
    return data




