import os
import sys
import pandas as pd
import pickle
from src.BookRecommendationSystem.logger import logging
from src.BookRecommendationSystem.exception import customexception
import numpy as np
from src.BookRecommendationSystem.utlis.utils import save_object

class datatransformationconfig:
    data=os.path.join("artifacts","data.pkl")
class data_transformation2:
    def __init__(self):
        self.allpath=datatransformationconfig()
        
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
          ratingatleast200user=book_and_rating.groupby('User-ID')['Book-Rating'].count().reset_index()
          ratingatleast200user.rename(columns={'Book-Rating':'Book-Rating_count'},inplace=True)
          atleast200ratinguser=ratingatleast200user[ratingatleast200user['Book-Rating_count']>=200]
          x=pd.unique(atleast200ratinguser['User-ID'])
          filter_data=book_and_rating[book_and_rating['User-ID'].isin(x)]
          logging.info("get data where users gave atlist 200 ratings")
          c1=filter_data.groupby('Book-Title')['Book-Rating'].count().reset_index()
          c1.rename(columns={'Book-Rating':'Book-Rating_count'},inplace=True)
          atlest50_rating=c1[c1['Book-Rating_count']>=50]
          v=pd.unique(atlest50_rating['Book-Title'])
          final_data2=filter_data[filter_data['Book-Title'].isin(v)]
          logging.info("get data where users gave atlist 200 ratings and book has atleast 50 rating")
          data=final_data2.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')
          data.fillna(0,inplace=True)
          save_object(obj=data,file_path=self.allpath.data)
          return self.allpath.data
          logging.info("get final data for model training")
       except Exception as e:
          logging.info("exception during occured at data tarnsformation initiation stage")
          raise customexception(e,sys)



