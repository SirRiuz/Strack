

# Libs
from typing import Union
from fastapi import FastAPI, Request
from consumers.testing import TestConsumer
from core.pagination import Pagination
import time


app = FastAPI()


@app.get("/api/v1/search/")
async def search(
    request:Request,
    q:Union[str,None]='Unknow',
    min:Union[int,None]=0,
    max:Union[int,None]=5,
    
    # Filter params
    is_descount:Union[bool,None]=False,
    is_free_shipping:Union[bool,None]=False,
    score:Union[float,None]=None,
    range:Union[str,None]=''
):
    
    start = time.time()
    result = TestConsumer().search(
        keyboard=q.lower(),
        options={
            'is_descount':is_descount,
            'is_free_shipping':is_free_shipping,
            'range':range,
            'score':score
        }
    )
    pagination = Pagination(
        min=min,max=max,data=result['data'],
        context={
            'base_url':request.base_url,
            'query':result['query']
        }
    ).paginate()
    end = time.time()
    
    
    return ({
        'meta':{
            'total-size':len(result['data']),
            'cache':result['is_cache'],
            'query':result['query'],
            'time-response':f'{int(end - start)}s',
            'data-providers':result['providers']
        },
        'pagination':{
            'size':len(pagination['results']),
            'next':pagination['next_url']
        },
        'data':result['data'],   #BUG
        'status':'ok'
    })






