import os
import sys

from src.BookRecommendationSystem.logger import logging
from src.BookRecommendationSystem.exception import customexception
from src.BookRecommendationSystem.components.data_ingestion import data_ingestion
from src.BookRecommendationSystem.components.data_transformation import data_transformation




obj1=data_ingestion()
book,user,rating=obj1.initiate_data_ingestion()

obj2=data_transformation()
top50=obj2.data_transform_initiated(book,rating)