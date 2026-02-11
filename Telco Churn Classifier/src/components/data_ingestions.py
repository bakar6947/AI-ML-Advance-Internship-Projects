import os
import sys
import pandas as pd
from logger import logging
from sklearn.model_selection import train_test_split




# Confugure Data Ingestion Files
class DataIngestionConfig:
    try:
        logging.info('Data Ingestion Config Start')
        raw_data_file = os.path.join('artifact', 'raw.csv')
        train_data_file = os.path.join('artifact', 'train.csv')
        test_data_file = os.path.join('artifact', 'test.csv')
        logging.info('Data Ingestion Config Complete')
    except Exception as e:
        logging.error(f'Error in Data Ingestion Config: {e}')




# Perform Data Ingestion
class DataIngestion:

    def __init__(self):
        self.ingestion_config_obj = DataIngestionConfig()

    # Perform Train Test Split and Save DataFrames as CSV into Artifact
    def split_data(self):

        try:
            logging.info('Data Ingestion Start')

            # Load Data Set
            df = pd.read_csv("D:\AI-ML\Projects\AI Internship Projects Part_2\Telco Churn Classifier\data\Telco_Churn_Dataset.csv")
            logging.info('Data Set Loaded Successfully ')


            # Create artifact Directory
            artifact_path = os.path.dirname(self.ingestion_config_obj.raw_data_file)
            os.makedirs(artifact_path, exist_ok=True)
            logging.info('Artifact Directory Created Successfully ')


            # # Perform Train Test Split
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
            logging.info('Train Test Split Performed Successfully ')


            # # Save Raw, Test and Train DataFrames as CSV into Artifact
            df.to_csv(self.ingestion_config_obj.raw_data_file, index=False) 
            train_df.to_csv(self.ingestion_config_obj.train_data_file, index=False)
            test_df.to_csv(self.ingestion_config_obj.test_data_file, index=False)
            logging.info('Data Ingestion Completed Successfully')


            return(
                self.ingestion_config_obj.train_data_file,
                self.ingestion_config_obj.test_data_file
            )

        except Exception as e:
            logging.error(f'Error in Data Ingestion: {e}')