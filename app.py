from flask import Flask,render_template,redirect

from flask import request
import  numpy as np
import pickle
import pandas as pd

pickle_model=open("wcclassifier.pkl","rb")
classifier=pickle.load(pickle_model)

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict' , methods = ['POST' , 'GET'])
def predict():
    match = [x for x in request.form.values()]
    rankingdf = {
        'India': 1,
        'Australia': 2,
        'pakistan': 3,
        'South Africa': 4,
        'New Zealand': 5,
        'England': 6,
        'Sri Lanka': 7,
        'Bangladesh': 8,
        'Afghanistan': 9,
        'Netherlands': 10, 
    }
    team1 = match[0]
    team2 = match[1]
    position1 = 11 - rankingdf[team1]
    position2 = 11 - rankingdf[team2]

    df = pd.read_csv('finaldf.csv')
    df.drop(['sn'] , axis = 1 , inplace=True)
    data = {
        'Team 1': [team1],
        'Team 2': [team2],
        "Team 1 Position": [position1],
        "Team 2 Position": [position2]
    }
    df_temp = pd.DataFrame(data)
    pred_set = pd.get_dummies(df_temp, prefix=['Team 1', 'Team 2'], columns=['Team 1', 'Team 2'])
    missing_cols2 = set(df.columns) - set(pred_set.columns)
    # print(missing_cols2)
    for c in missing_cols2:
        pred_set[c] = 0
    pred_set = pred_set[df.columns]

    pred_set = pred_set.drop(['Winner'], axis=1)
    print(pred_set)
    pred = classifier.predict(pred_set)
    index = pred.argmax()
    variable = pred[0]
    
    return render_template('index.html', outputpredicted  = variable)
            

if __name__  == '__main__':
    app.run(debug=True)