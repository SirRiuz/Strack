



import json
from core.sekeer import Sekeer
from bs4 import BeautifulSoup
import ast

# bs = BeautifulSoup(open('data.html','r').read(),'html.parser')
data = json.loads(open('data.json','r').read())
result = Sekeer().find(
    data=data,
    query='"<items/>"',
    #type_render='html',
    many=True
)
print(data)

# <span::a-spinner a-spinner-medium#many/>
# <span::a-size-small a-color-base/>

