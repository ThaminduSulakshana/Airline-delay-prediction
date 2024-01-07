
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
from app import app 

# Load the trained model from the pickle file
with open('Flightdelay_rf_model.pickle', 'rb') as model_file:
    rf_model = pickle.load(model_file)



@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input features from the form
        year = int(request.form['year'])
        month = int(request.form['month'])
        arr_time = int(request.form['arr_time'])
        distance = int(request.form['distance'])

        # Make a prediction using the trained model
        prediction = rf_model.predict(np.array([year, month, arr_time, distance]).reshape(1, -1))

        # Render the result template with the prediction
        return render_template('index.html', prediction=prediction[0])
    except Exception as e:
        # Handle errors and return an appropriate response
        return render_template('error.html', error_message=str(e))
