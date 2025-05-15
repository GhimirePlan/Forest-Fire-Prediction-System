from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Check if pickle files exist
if not os.path.exists('model.pkl') or not os.path.exists('scaler.pkl'):
    print("Error: model.pkl or scaler.pkl not found!")
    exit(1)

try:
    # Load the trained model and scaler
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    print("Model and scaler loaded successfully!")
    
except Exception as e:
    print(f"Error loading models: {e}")
    print("Please recreate the pickle files with recreate_models.py")
    exit(1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [
            float(request.form['temperature']),
            float(request.form['rh']),
            float(request.form['ws']),
            float(request.form['rain']),
            float(request.form['ffmc']),
            float(request.form['dmc']),
            int(request.form['classes'])
        ]
        
        # Convert to numpy array and reshape
        features_array = np.array(features).reshape(1, -1)
        
        # Scale the features
        features_scaled = scaler.transform(features_array)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        
        # Format prediction
        prediction = round(prediction, 2)
        
        return render_template('result.html', prediction=prediction, features=features)
        
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)