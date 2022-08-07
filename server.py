


# Libs
from flask import Flask,request
from httplib2 import Response
from consumers.testing import TestConsumer
from settings import API_VERSION, DEBUG
import time
from storage import get_to_storage



app = Flask(__name__)



@app.errorhandler(500)
def internal_error(e):
    return ({
        'status':'error',
        'error':{'messege':str(e)}
    },500)




@app.route(f'/{API_VERSION}/search/',methods=['GET'])
def search() -> (Response):
    """
      Esta ruta es la encargada de realizar
      las busquedar y mostrarme los resultados.
    """
    start = time.time()
    query = request.args.get('q')
    storage_data = get_to_storage(query)
    result = TestConsumer().search(
        query.lower(),
        filter={
            'score':request.args.get('score'),
            'range':request.args.get('range')
        },
        cache=storage_data
    )
    end = time.time()
    
    return ({
        'status':'ok',
        'meta':{
            'length':len(result['data']),
            'query':query,
            #'provider':None,
            #'limit':None,
            'time-response':f'{int(end - start)}s',
            'providers':result['providers'],
            'cache':bool(storage_data)
        },
        'data':result['data']
    },200)






app.run(
    host='0.0.0.0',
    debug=DEBUG
)



