import os
import sys
import pickle
import pandas as pd
from logger import logging
from exceptions import CustomException
from sklearn.metrics import accuracy_score, recall_score, f1_score





# Save Pickle Object
def save_pickle_obj(model_obj, file_path):
    try:
        logging.info('Saving Transformation Pipeline as Pickle Object')
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, 'wb') as file:
            pickle.dump(model_obj, file)
        
        logging.info('Pickle Object Saved Successfully')

    except Exception as e:
        logging.error(f'Error Saving Pickle Object: {e}')
        raise CustomException(e, sys)
    


# Load Pickle Object
def load_pickle_obj(file_path):

    try:
        logging.info('Loading Pickle Object')
        with open(file_path, 'rb') as file:
            file_obj = pickle.load(file=file)

            logging.info("Pickle Object Load Successfully")
            return file_obj

    except Exception as e:
        logging.error(f'Error Loading Pickle Object: {e}')
        raise CustomException(e, sys)
    





def model_evaluation(models, X_train, X_test, y_train, y_test):

    try: 
        logging.info('Model Evaluation Start')
        scores = []

        for key, value in models.items():

            model = value
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            accuracy = accuracy_score(y_test, y_pred)

            results = {
                'Model': key,
                'Recall Score': recall,
                'F1 Score': f1,
                'Accuracy': accuracy
            }
            scores.append(results)
        
        evaluation_data = pd.DataFrame(scores)
        evaluation_data = evaluation_data.sort_values(by='Accuracy')
        logging.info('Model Evaluation Completed Successfully')
        return evaluation_data

    
    except Exception as e:
        logging.error(f'Error in Model Evaluation: {e}')
        raise CustomException(e, sys)