import numpy as np
from flask import Flask, request, jsonify, render_template
#import pickle
import joblib

app = Flask(__name__)
#model = pickle.load(open('model.joblib', 'rb'))
model = joblib.load('model1.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.forecast(steps = final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Future days revenue:  $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)