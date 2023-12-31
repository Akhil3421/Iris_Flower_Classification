import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd



app=Flask(__name__)
#load the model
model=pickle.load(open('svc.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    new_data=np.array(data).reshape(1,-1)
    output=model.predict(new_data)
    print(output[0])
    return jsonify(output[0])


@app.route('/predict',methods=['POST'])
def predict():
    data=[x for x in request.form.values()]
    final_input=np.array(data).reshape(1,-1)
    print(final_input)
    output=model.predict(final_input)[0]
    return render_template("home.html",prediction_text="The Flower is classified as {}".format(output))



if __name__=="__main__":
    app.run()