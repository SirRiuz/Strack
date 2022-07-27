


# Libs
from flask import Flask,request
from httplib2 import Response
from consumers.testing import TestConsumer
from settings import API_VERSION, DEBUG
import time

from storage import add_to_storage, get_to_storage



app = Flask(__name__)




@app.errorhandler(500)
def internal_error(e):
    return ({
        'status':'error',
        'error':{
            'messege':str(e)
        }
    },500)






@app.route(f'/{API_VERSION}/search/',methods=['GET'])
def search() -> (Response):
    start = time.time()
    cacheMode = True
    query = request.args.get('q')
    
    
    data = get_to_storage(query)
    
    if not data:
        data = TestConsumer().search(query.lower())
        add_to_storage(query,data)
        cacheMode = False
    
    
    end = time.time()
    
    return ({
        'status':'ok',
        'meta':{
            'length':len(data['data']),
            'query':query,
            #'provider':None,
            #'limit':None,
            'time-response':f'{int(end - start)}s',
            'providers':data['providers'],
            'cache':cacheMode
        },
        'data':data['data']
    },200)






app.run(
    debug=DEBUG
)



