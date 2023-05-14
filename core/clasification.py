

# libs
import unidecode
from helpers.dataset import load_dataset
from textblob.classifiers import NaiveBayesClassifier

# consumers
from consumers.mapping import CONSUMER_MAPPING
from core.consumer import BaseConsumer


class Clasification:
    
    def __init__(self) -> (None):
        self.cl = NaiveBayesClassifier(load_dataset())
        self.category = None
    
    def get_provider(self,query:str) -> (BaseConsumer):
        category = self.cl.classify(self.__clear_query(query))
        self.category = category
        return self.__get_instance(category)
    
    def __clear_query(self,query:str) -> (str):
        return unidecode.unidecode(query.lower().replace('\n',''))
    
    def __get_instance(self,category:str) -> (object):
        return CONSUMER_MAPPING[category]
        



