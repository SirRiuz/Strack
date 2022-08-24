

#from providers.linio.provider import *
#from consumers.music import MusicConsumer
#from consumers.smartphone import SmartPhoneConsumer
#from providers.olx.provider import *
#from providers.mercadolibre.provider import *
#from providers.linio.provider import *
#from providers.falabella.provider import *
import json
from consumers.testing import TestConsumer
from core.pagination import Pagination



result = TestConsumer().search('redmi note 9'.lower())
pagination = Pagination(min=10,max=11,data=result['data'])

#pagination.get_pagination_data()
print(json.dumps(pagination.get_pagination_info(),indent=2))


