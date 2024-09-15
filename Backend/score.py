import json
import joblib
import numpy as np
from azureml.core.model import Model
from flask import Flask, request, jsonify

app = Flask(__name__)

def init():
    global model
    try:
        # Load the model from the registered model
        model_path = Model.get_model_path('crime_model.pkl')
        model = joblib.load(model_path)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = np.array(data['data'])
        predictions = model.predict(input_data)
        
        # Assuming the model returns cluster labels
        clusters = predictions.tolist()
        
        # Return the cluster information
        return jsonify({'clusters': clusters})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0', port=5000)