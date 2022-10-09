


# Libs
from time import time
from typing import Union

from app.consumers.testing import TestConsumer



def handler(event,context) -> (dict):
    q:Union[str,None] = event.get('q','Unknow')
    is_descount:Union[bool,None]=event.get('is_descount','Unknow'),
    is_free_shipping:Union[bool,None]=event.get('is_free_shipping','Unknow'),
    score:Union[float,None]=event.get('score','Unknow'),
    range:Union[str,None]=event.get('range','Unknow')

    result = TestConsumer().search(
        keyboard=q.lower(),
        options={
            'is_descount':is_descount,
            'is_free_shipping':is_free_shipping,
            'range':range,
            'score':score
        }
    )
    print(result)

    return ({
        'hello':'hello'
    })







