# Python
import time
from typing import Union

# FastApi
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Libs
from core.pagination import Pagination
from consumers.electronic import ElectronicConsumer


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
provider = ElectronicConsumer()

@app.get("/api/v1/search/")
async def search(
    request:Request,
    q:Union[str,None]='Unknow',
    min:Union[int,None]=0,
    max:Union[int,None]=20,
    
    # Filter params
    is_descount:Union[bool,None]=False,
    is_free_shipping:Union[bool,None]=False,
    score:Union[float,None]=None,
    range:Union[str,None]=''
):
    
    start = time.time()
    result = provider.search(
        keyboard=q.lower(),
        options=({
            'is_descount':is_descount,
            'is_free_shipping':is_free_shipping,
            'range':range,
            'score':score
        })
    )
    pagination = Pagination(
        min=min,max=max,data=result['data'],
        context=({
            'base_url':request.base_url,
            'query':result['query']
        })).paginate()
    
    end = time.time()
    
    return ({
        'meta':{
            'total-size':len(result['data']),
            'cache':result['is_cache'],
            'query':result['query'],
            'time-response':f'{int(end - start)}s',
            'data-providers':result['providers'],
        },
        'pagination':{
            'size-page':len(pagination['data']),
            'next':pagination['next']
        },
        'data':pagination['data']
    })
