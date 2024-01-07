from app import app
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model from the pickle file
with open('Flightdelay_rf_model.pickle', 'rb') as model_file:
    rf_model = pickle.load(model_file)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the form
    year = int(request.form['year'])
    month = int(request.form['month'])
    
    arr_time = int(request.form['arr_time'])
    distance = int(request.form['distance'])

    # Make a prediction using the trained model
    prediction = rf_model.predict(np.array([year, month, arr_time, distance]).reshape(1, -1))

    # Render the result template with the prediction
    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
