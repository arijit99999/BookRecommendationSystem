import flask
import pickle
import os
import pandas as pd
from flask import Flask, render_template,request
from src.BookRecommendationSystem.utlis.utils import load_object
import numpy as np

top50=pd.read_csv(r'C:\Users\deyar\OneDrive\Desktop\BookRecommendationSystem\artifacts\top50.csv')
with  open('model.pkl','rb') as file:
 similarity=pickle.load(file)
book=pd.read_csv(r'C:\Users\deyar\OneDrive\Desktop\BookRecommendationSystem\artifacts\book.csv')
data=pd.read_csv(r'C:\Users\deyar\OneDrive\Desktop\BookRecommendationSystem\artifacts\data.csv')
app=Flask(__name__,template_folder='template')
@app.route('/')
def index():
         return render_template('index.html',
                            book_name=list(top50['Book-Title'].values),
                            author=list(top50['Book-Author'].values),
                            image=list(top50['Image-URL-M'].values),
                            vote=list(top50['rating_count'].values),
                            rating=list(top50['rating_avg'].values))
        
@app.route('/result')
def form():
          return render_template('form.html')
@app.route('/resultop',methods=['post'])
def form1():
         user_input = request.form.get('user_input')
         index=np.where(data.index==user_input)[0][0]
         similar=sorted(list(enumerate(similarity[index])),key=lambda x:x[1],reverse=True)[1:6]
         res=[]
         for i in similar:
           item=[]
           temp=book[book['Book-Title']==data.index[i[0]]]
           item.extend(temp.drop_duplicates('Book-Title')['Book-Title'].values)
           item.extend(temp.drop_duplicates('Book-Title')['Book-Author'].values)
           item.extend(temp.drop_duplicates('Book-Title')['Image-URL-M'].values)
           res.append(item)
         return render_template('form.html',data=res)
if __name__=="__main__":
 app.run(debug=True)













