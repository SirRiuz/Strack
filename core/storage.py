# Libs
import hashlib
import json
import os
import datetime
from settings import STORAGE_DIR


def get_to_storage(query:str) -> (dict):
    query_hash = hashlib.sha256(query.encode()).hexdigest()
    STORAGE_ITEM_DIR = f'{STORAGE_DIR}/{query_hash}'
    
    if os.path.exists(STORAGE_ITEM_DIR):
        data = json.loads(open(STORAGE_ITEM_DIR,'r').read())
        create = datetime.datetime.strptime(
            data['expire'],'%d-%m-%Y %H:%M')
        now = datetime.datetime.now()
        result = now - create
        
        if result.days >= 1 or result.days < 0:
            os.remove(STORAGE_ITEM_DIR)
            return
            
        return data


def add_to_storage(query:str,data:dict) -> (bool):
    storage_dir = os.listdir(STORAGE_DIR)
    query_hash = hashlib.sha256(query.encode()).hexdigest()
    
    if not query_hash in storage_dir:
        open(f'{STORAGE_DIR}/{query_hash}','w').write(json.dumps({
            'expire':datetime.datetime.now()\
                .strftime('%d-%m-%Y %H:%M'),
            'data':data.get('data'),
            'providers':data.get('providers')
        },indent=2))
        return True
    
    
    

