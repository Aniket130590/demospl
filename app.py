from flask import Flask, request, jsonify, render_template
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
   
      
    df=pd.read_csv('consolidated.csv')
    df = df[df['name'].str.find("ABBA") != -1]  
    
    def get_ratio(row):
        name = row['name']
        return fuzz.token_sort_ratio(name, "ABBAS")

    def get_ratio2(row):
        name = row['addresses']
        return fuzz.token_sort_ratio(name, "SY")

    df1 = df[df.apply(get_ratio, axis=1) > 50]
    df2 = df1[df1.apply(get_ratio2, axis=1) > 10]

    #return render_template('index.html', prediction_text=df)
    return render_template('index2.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)



if __name__ == "__main__":
    app.run(debug=True)