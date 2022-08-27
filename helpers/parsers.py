

import json
from bs4 import BeautifulSoup
from core.models import BaseProductModel
from core.sekeer import Sekeer



def parse_price(price):
    price = price.replace('.','') if type(price) is str else price
    price = price.replace(',','') if type(price) is str else price
    price = price.replace('COP $','') if type(price) is str else price
    price = price.replace(' ','') if type(price) is str else price
    price = int(price) if type(price) is str else price
    return price



def parse_htm(html_data:str,dataset:str,model:BaseProductModel) -> (tuple):
    
    """ Se encarga de parcear una respuesta de tipo html """
    
    split_query = dataset.split('::')
    query = split_query[1]
    tag = split_query[0]
    soup = BeautifulSoup(html_data,'html.parser')
    dataset = soup.find_all(tag,class_=query)
    data = []

    for item in dataset:

        # actual_price
        actual_price = item.find(class_=model.actual_price)
        actual_price = actual_price.text if actual_price else None
        
        # free_shipping
        free_shipping = bool(item.find(class_=model.free_shipping))

        # discount
        discount_label = item.find(class_=model.discount_label)
        discount_label = discount_label.text if discount_label else None
        is_discount = bool(discount_label)
        #discount = item.find(class_='a-price a-text-price puis-light-weight-text')
        #discount = discount.text if discount else None
        
        # Preview
        preview = item.find(class_=model.preview)['src']
        name = item.find(class_=model.name).text
        name = name.lower() if name and type(name) is str else ''
        origin = item.find(class_=model.origin)['href']
        
        
        data.append({
            'name':name,
            'preview':preview,
            'origin':origin,
            'actual_price':parse_price(actual_price),
            'is_descount':is_discount,
            'original_price':None,
            'is_free_shipping':free_shipping,
            #'score':'',
            #'description':'',
            'discount_label':discount_label
        })
        
    
    return data




def parse_json(json_data:str,dataset:str,model:BaseProductModel) -> (tuple):
    
    """ Se encarga de parcear una respuesta de tipo JSON """
    
    sekeer = Sekeer()
    data = []
    dataset = sekeer.find(json.loads(json_data),dataset)
    
    
    for item in (dataset if dataset else []):
                
        # discount
        actual_price = sekeer.find(item,model.actual_price)
        original_price = sekeer.find(item,model.original_price)
        discount_label = sekeer.find(item,model.discount_label)
        is_discount = bool(discount_label)
        
        free_shipping = bool(sekeer.find(item,model.free_shipping))
        score = sekeer.find(item,model.score)
        score = score if score else 0
        score = 5 if score > 5 else score
        description = sekeer.find(item,model.description)
        
        preview = sekeer.find(item,model.preview)
        name = sekeer.find(item,model.name)
        name = name.lower() if name and type(name) is str else ''
        origin = sekeer.find(item,model.origin)
        

        data.append({
            'name':name,
            'preview':preview,
            'origin':origin,
            'actual_price':parse_price(actual_price),
            'is_descount':is_discount,
            'original_price':parse_price(original_price),
            'is_free_shipping':free_shipping,
            'score':score,
            'description':description,
            'discount_label':discount_label
        })
        
    
    
    return data




