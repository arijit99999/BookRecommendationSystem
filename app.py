import flask
import pickle
import os
import pandas as pd
from flask import Flask, render_template,request
import warnings
warnings.filterwarnings('ignore')
import numpy as np

top50=pd.read_csv(r'C:\Users\deyar\OneDrive\Desktop\BookRecommendationSystem\artifacts\top50.csv')
similarity=pickle.load(open('model.pkl','rb'))
book=pd.read_csv(r'C:\Users\deyar\OneDrive\Desktop\BookRecommendationSystem\artifacts\book.csv')
final_data=pickle.load(open('data.pkl','rb'))
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
  user_input = str(request.form.get('user_input'))
  index=np.where(final_data.index==user_input)[0][0]
  similar=sorted(list(enumerate(similarity[index])),key=lambda x:x[1],reverse=True)[1:5]
  data=[]
  for i in similar:
           item=[]
           temp=book[book['Book-Title']==final_data.index[i[0]]]
           item.extend(temp.drop_duplicates('Book-Title')['Book-Title'].values)
           item.extend(temp.drop_duplicates('Book-Title')['Book-Author'].values)
           item.extend(temp.drop_duplicates('Book-Title')['Image-URL-M'].values)
           data.append(item)
  return  render_template('form.html',data=data)
if __name__=="__main__":
 app.run(debug=True)













