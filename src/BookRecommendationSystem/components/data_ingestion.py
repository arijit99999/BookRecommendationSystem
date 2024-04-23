import pandas as pd
import os
import sys
import warnings
from src.BookRecommendationSystem.logger import logging
from src.BookRecommendationSystem.exception import customexception

class dataingestionConfig:
    raw_data_book=os.path.join("artifacts","book.csv")
    raw_data_user=os.path.join("artifacts","user.csv")
    raw_data_rating=os.path.join("artifacts","rating.csv")


class data_ingestion:
    def __init__(self):
        self.ingestion_config=dataingestionConfig()
        
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        
        try:
           warnings.filterwarnings('ignore')
           book=pd.read_csv(r'C:\Users\deyar\OneDrive\Desktop\BookRecommendationSystem\notebooks\data\Books.csv') 
           os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_book)),exist_ok=True) 
           book.to_csv(self.ingestion_config.raw_data_book,index=False) 
           logging.info('book data saved ')  

           user=pd.read_csv(r'C:\Users\deyar\OneDrive\Desktop\BookRecommendationSystem\notebooks\data\Users.csv')   
           user.to_csv(self.ingestion_config.raw_data_user,index=False)
           logging.info("saved user data")

           rating=pd.read_csv(r'C:\Users\deyar\OneDrive\Desktop\BookRecommendationSystem\notebooks\data\Ratings.csv') 
           rating.to_csv(self.ingestion_config.raw_data_rating,index=False)
           logging.info('saved rating data')

           return (self.ingestion_config.raw_data_book,
                   self.ingestion_config.raw_data_user,
                   self.ingestion_config.raw_data_rating)
        except Exception as e:
           logging.info("exception during occured at data ingestion stage")
           raise customexception(e,sys)