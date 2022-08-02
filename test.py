



#from providers.linio.provider import *


#from consumers.music import MusicConsumer
#from consumers.smartphone import SmartPhoneConsumer
#from providers.olx.provider import *
#from providers.mercadolibre.provider import *
#from providers.linio.provider import *
#from providers.falabella.provider import *
from consumers.testing import TestConsumer


result = TestConsumer().search('Calculadora cientifica en oferta con graficadora'.lower())



