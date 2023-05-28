# Python
import os


DEBUG = True

# DIRS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROVIDERS_DIR = 'providers/'
COMMANDS_DIR = 'commands/'
STORAGE_DIR = os.path.join(BASE_DIR, 'storage')
SERVICE_DIR = os.path.join(BASE_DIR, 'services')
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')


if not os.path.exists(STORAGE_DIR):
    os.mkdir(STORAGE_DIR)
