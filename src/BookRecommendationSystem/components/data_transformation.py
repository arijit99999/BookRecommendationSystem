import os
import sys
import pandas as pd
import pickle
from src.BookRecommendationSystem.logger import logging
from src.BookRecommendationSystem.exception import customexception
import numpy as np
from src.BookRecommendationSystem.utlis.utils import save_object

class datatransformationconfig:
    top50=os.path.join("artifacts","top50.csv")
class data_transformation:
    def __init__(self):
        self.top50_path=datatransformationconfig()
        
    def data_transform_initiated(self,book,rating):
       try:
          logging.info('trasnformation initiated')
          book=pd.read_csv(book)
          rating=pd.read_csv(rating)
          logging.info("read book and rating data")
          book_and_rating=book.merge(rating,on='ISBN')
          logging.info("merge book and rating dataset")
          book_and_rating.dropna(inplace=True)
          logging.info("drop book and rating dataset's null value")
          count=book_and_rating.groupby('Book-Title')['Book-Rating'].count().reset_index()
          count=count.rename(columns={'Book-Rating':'rating_count'})
          logging.info("add new column rating frequency")
          avg=book_and_rating.groupby('Book-Title')['Book-Rating'].mean().reset_index()
          avg=avg.rename(columns={'Book-Rating':'rating_avg'})
          logging.info("add new column rating avg")
          count_avg=count.merge(avg,on='Book-Title')
          logging.info("merge columns rating_avg and rating_frquency")
          popular_book=count_avg[count_avg['rating_count']>250]
          logging.info("extarct row which rating frequency is more than 250 and that's why this is popular")
          popular_book=popular_book.sort_values(by='rating_count',ascending=False).head(50)
          logging.info("extarct top 50 rows which rating frequency is more than 250 ")
          popular_book50=popular_book.merge(book,on='Book-Title')
          logging.info("merge top 50 data and real book data")
          final50=popular_book50.drop_duplicates('Book-Title')
          final50=final50[['Book-Title','Image-URL-M','Book-Author','rating_count','rating_avg']]
          logging.info("get top 50 book's data")
          topbook=final50.to_csv(self.top50_path.top50,index=False)
          return topbook
          logging.info("get top50.pkl")
       except Exception as e:
          logging.info("exception during occured at data tarnsformation initiation stage")
          raise customexception(e,sys)



