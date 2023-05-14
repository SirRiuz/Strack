
# Libs
import os


DEBUG = True


# DIRS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STORAGE_DIR = os.path.join(BASE_DIR,'storage')
SERVICE_DIR = os.path.join(BASE_DIR,'services')
DATASET_DIR = os.path.join(BASE_DIR,'dataset')


if not os.path.exists(STORAGE_DIR):
    os.mkdir(STORAGE_DIR)


# AWS CREDENTIALS
AWS_SECRET_ACCESS_KEY = 'DZGPxbN0SjewL1MmGDHiJ9C7RNq3dAXn9R0fJ0+W'
AWS_ACCESS_KEY_ID = 'AKIAZ4JLB3PXV57BRHZJ'
