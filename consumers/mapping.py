

#consumers
from .electronic import ElectronicConsumer
from .tech import TechConsumer
from .pets import PetsConsumer
from .fashion import FashionConsumer
from .gym import GymConsumer


CONSUMER_MAPPING = {
    'electronic':ElectronicConsumer(),
    'tech':TechConsumer(),
    'pets':PetsConsumer(),
    'pashion':FashionConsumer(),
    'gym':GymConsumer()
}



