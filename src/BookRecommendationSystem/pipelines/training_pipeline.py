import os
import sys
from src.BookRecommendationSystem.logger import logging
from src.BookRecommendationSystem.exception import customexception


from src.BookRecommendationSystem.components.data_ingestion import data_ingestion
from src.BookRecommendationSystem.components.data_transformation import data_transformation
from src.BookRecommendationSystem.components.data_transformation2 import data_transformation2
from src.BookRecommendationSystem.components.model_trainer import ModelTrainer



obj1=data_ingestion()
book,user,rating=obj1.initiate_data_ingestion()

obj2=data_transformation()
top50=obj2.data_transform_initiated(book,rating)


obj3=data_transformation2()
data=obj3.data_transform_initiated(book,rating)


obj4=ModelTrainer()
obj4.initate_model_training()

