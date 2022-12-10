import os,sys
from sensor.entity import config_entity,artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
from typing import Optional
import pandas as pd


class DataValidation:

    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20}Data Validataion{'<<'*20}")
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise SensorException(e, sys)

    def drop_missing_values_columns(self,df:pd.DataFrame,threshold:float=0.3)->Optional[pd.DataFrame]:
        """
        This function will drop column which contain missing value more than specified threshold

        df: Accepts a pandas dataframe
        threshold: Percentage criteria to drop a column
        ==========================================================================================
        returns Pandas DataFrame if atleast a single column is available after missing columns drop else None
        """
        try:
            null_report = df.isna().sum()/df.shape[0]
            #selecting column name which contains null
            logging.info(f"selecting column name which contains null above to {threshold}")
            drop_column_names = null_report[null_report>threshold].index

            #return the None no column left
            if len(df.column) == 0:
                return None
            return df
        except Exception as e:
            raise SensorException(e, sys)

    def is_required_columns_exist(self)->bool:
        pass

    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:...