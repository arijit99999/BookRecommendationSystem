import os
import sys
import pandas as pd
import pickle
from src.BookRecommendationSystem.logger import logging
from src.BookRecommendationSystem.exception import customexception
from sklearn.metrics.pairwise import cosine_similarity
from src.BookRecommendationSystem.utlis.utils import save_object


 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initate_model_training(self):
        try:
            data=pickle.load(open('data.pkl','rb'))
            similarity=cosine_similarity(data) 
            save_object(obj=similarity,file_path=self.model_trainer_config.trained_model_file_path)
            logging.info('model saved')
        except Exception as e:
          logging.info("exception occured during model trainig stage")
          raise customexception(e,sys)