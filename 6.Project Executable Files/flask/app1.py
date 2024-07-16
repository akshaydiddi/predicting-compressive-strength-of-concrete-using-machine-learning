import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
from sklearn.ensemble import GradientBoostingRegressor

# Load the pre-trained model
model = pickle.load(open(r'C:\Users\bhumi\Desktop\Project Executable Files\flask\cement.pkl', 'rb'))

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')

# Route for prediction page
@app.route('/index1',methods=['GET'])
def predict_now():
    return render_template('index1.html')

@app.route('/home')
def Home():
    return render_template('home.html')


@app.route('/home')
def About():
    return render_template('home.html')


@app.route('/home')
def Services():
    return render_template('home.html')


@app.route('/home')
def Team():
    return render_template('home.html')


@app.route('/home')
def Contact():
    return render_template('home.html')


@app.route('/result2',methods=['POST','GET'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    features_name  = ['Cement','Blast Furnace Slag','Fly Ash','Water','Superplasticizer','Coarse Aggregate','Fine Aggregate','Age']
    x = pd.DataFrame(features_value,columns=features_name)
    prediction = model.predict(x)
    print('prediction is',prediction)
    return render_template('result2.html',gbr=prediction)


# Route to handle prediction
if __name__ == ("__main__"):
    app.run(debug=False,port=5000)
