import os,sys 
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.entity import config_entity, artifact_entity
from sensor.utils import load_object
from sensor.predictor import ModelResolver
from skleran.metrics import f1_score 
import pandas as pandas
from sensor.config import TARGET_COLUMN

class ModelEvalution:

    def __init__(self,
        model_eval_config:config_entity.ModelEvaluationConfig,
        data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
        data_tranformation_artifact:artifact_entity.DataTransformationArtifact,
        model_trainer_artifact: artifact_entity.ModelTrainerArtifact
        ):
        try:
            logging.info(f"{'>>'*20}  Model Evaluation {'<<'*20}")
            self.model_eval_config= model_eval_config
            self.data_ingestion_artifact= data_ingestion_artifact
            self.data_tranformation_artifact = data_tranformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver()
        except Exception as e:
            raise SensorException(e, sys)
