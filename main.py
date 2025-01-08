import sys
import os

# Add 'src' directory to sys.path
sys.path.append(os.path.abspath("src"))

from MLOPS import logger
from MLOPS.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=======================x")
except Exception as e:
    logger.exception(e)
    raise e
