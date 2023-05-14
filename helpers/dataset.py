
# libs
import requests
import json
import os
import unidecode
from textblob.classifiers import NaiveBayesClassifier


# Settings
from settings import DATASET_DIR




def test_dataset():
    datalist = open('dataset/testing','r').readlines()
    cl = NaiveBayesClassifier(load_dataset())
    index_error = 0

    for line in datalist:
        line_data = line.split('#')
        TAG = line_data[1].replace('\n','')
        TITLE = line_data[0].lower()
        result = cl.classify(unidecode.unidecode(TITLE))
        
        if not result == TAG:
            print(f'[!] :: {TITLE}#{TAG} ----> {result}')
            index_error += 1
    
    print(f'\nERRORS : {index_error}/{len(datalist)}')


def get_dataset(query):
    url = f'https://frontend.mercadolibre.com/sites/MCO/search?dejavu=true&offset=0&limit=1000&q={query}&mclicsOn=true&pure_query=true'
    response = requests.get(url)
    data = json.loads(response.text)
    
    for item in data['results']:
        open(f'{DATASET_DIR}/{query}','a').write(f'{item["title"]}\n')


def load_dataset() -> (list):
    DATASET_FILES = os.listdir(DATASET_DIR)
    DATA_LIST = []
    for file_name in DATASET_FILES:
        FILE_DIR = f'{DATASET_DIR}/{file_name}'
        for line in open(FILE_DIR,'r').readlines():
            DATA_LIST.append(
                (unidecode.unidecode(
                    line.replace('\n','')
                ).lower(),file_name)
            )
    
    return DATA_LIST

#load_dataset()
#test_dataset()
#get_dataset('arena para gatos')

