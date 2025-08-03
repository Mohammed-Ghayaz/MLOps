from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<")

except Exception as e:
    logger.exception(e)
    raise e