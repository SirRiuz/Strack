



from typing import Union
from fastapi import FastAPI
from consumers.testing import TestConsumer
import time



app = FastAPI()


@app.get("/api/v1/search/")
async def search(q:Union[str,None]):
    start = time.time()
    result = TestConsumer().search(q)
    end = time.time()
    return {
        'data':result['data'][:14],
        'meta':{
            'size':len(result['data']),
            'cache':result['is_cache'],
            'query':q,
            'time-response':f'{int(end - start)}s'
        },
        'status':'ok'
    }





# # Libs
# from flask import Flask,request
# from httplib2 import Response
# from consumers.testing import TestConsumer
# from settings import API_VERSION, DEBUG
# import time



# app = Flask(__name__)



# @app.errorhandler(500)
# def internal_error(e):
#     return ({ 'status':'error','error':{'messege':str(e)} },500)




# @app.route(f'/{API_VERSION}/search/',methods=['GET'])
# def search() -> (Response):
#     """
#       Esta ruta es la encargada de realizar
#       las busquedar y mostrarme los resultados.
#     """
#     start = time.time()
#     query = request.args.get('q')
#     result = TestConsumer().search(
#         query.lower(),
#         filter={
#             'score':request.args.get('score'),
#             'range':request.args.get('range')
#         }
#     )
#     end = time.time()
    
#     return ({
#         'status':'ok',
#         'meta':{
#             'length':len(result['data']),
#             'query':query,
#             'time-response':f'{int(end - start)}s',
#             'providers':result['providers'],
#             'cache':result['is_cache']
#         },
#         'data':result['data']
#     },200)






# app.run(
#     host='0.0.0.0',
#     debug=DEBUG
# )



