

#from providers.linio.provider import *
#from consumers.music import MusicConsumer
#from consumers.smartphone import SmartPhoneConsumer
#from providers.olx.provider import *
#from providers.mercadolibre.provider import *
#from providers.linio.provider import *
#from providers.falabella.provider import *
import json
from consumers.testing import TestConsumer



result = TestConsumer().search('redmi note 9'.lower())
open('data.json','w').write(json.dumps(result,indent=2))



