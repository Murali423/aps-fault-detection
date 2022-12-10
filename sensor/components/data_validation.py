import os,sys
from sensor.entity import config_entity,artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
from typing import Optional
import pandas as pd
from sensor import utils


class DataValidation:

    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20}Data Validataion{'<<'*20}")
            self.data_validation_config = data_validation_config
            self.validation_error = dict()
        except Exception as e:
            raise SensorException(e, sys)

    def drop_missing_values_columns(self,df:pd.DataFrame)->Optional[pd.DataFrame]:
        """
        This function will drop column which contain missing value more than specified threshold

        df: Accepts a pandas dataframe
        ==========================================================================================
        returns Pandas DataFrame if atleast a single column is available after missing columns drop else None
        """
        try:
            threshold = self.data_validation_config.missing_threshold
            null_report = df.isna().sum()/df.shape[0]
            #selecting column name which contains null
            logging.info(f"selecting column name which contains null above to {threshold}")
            drop_column_names = null_report[null_report>threshold].index
            
            self.validation_error["dropped_columns"] =  list(drop_column_names)
            df.drop(list(drop_column_names), axis=1, inplace = True)

            #return the None no column left
            if len(df.column) == 0:
                return None
            return df
        except Exception as e:
            raise SensorException(e, sys)

    def is_required_columns_exist(self,base_df:pd.DataFrame,current_df:pd.DataFrame)->bool:
        try:
            base_columns = base_df.columns
            current_columns = current_df.columns

            missing_columns = []
            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.append(base_column)
            
            if len(missing_columns)>0:
                self.validation_error["Missing columns"] = missing_columns
                return False
            return True

        except Exception as e:
            raise SensorException(e, sys)

    def data_drift(self,base_df:pd.DataFrame,current_df:pd.DataFrame):
        try:
            drift_report = dict()


            base_columns = base_df.columns
            current_columns = current_df.columns

            for base_column in base_columns:
                base_data,current_data = base_df[base_column],current_df[base_column]

                same_distribution = ks_2samp(base_data,current_data)

                if same_distribution.pvalue > 0.05:
                    # We are accepting null hypothesis
                    drift_report[base_column]={
                        "pvalue":float(same_distribution.pvalue),
                        "same_distribution": True
                    }
                else: 
                    drift_report[base_column]={
                        "pvalue":float(same_distribution.pvalue),
                        "same_distribution": False
                    }
                    #different distribution
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        try:
            pass


        except Exception as e:
            raise SensorException(e, sys)