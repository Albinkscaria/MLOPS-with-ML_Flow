#from MLOPS import logger


import sys
import os

# Add 'src' directory to sys.path
sys.path.append(os.path.abspath("src"))

from MLOPS import logger
logger.info("Welcome to our custom logging")
