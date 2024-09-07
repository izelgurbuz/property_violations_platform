from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import json
import joblib

app = Flask(__name__)
CORS(app)

# Load the encoders and scaler
with open('data/mappings.json', 'r') as f:
    encoders = json.load(f)

violation_type_code_classes = encoders['violation_type_code']
street_classes = encoders['street']
boro_classes = encoders['boro']
house_number_classes = encoders['house_number']
violation_category_classes = encoders['violation_category']

# Load the trained model and scaler
model = tf.keras.models.load_model('models/task_priority_model.h5')
scaler = joblib.load('models/scaler.pkl')

@app.route('/violation-data', methods=['GET'])
def get_violation_data():
    return jsonify({
        "violation_type_code": violation_type_code_classes,
        "street": street_classes,
        "boro": boro_classes,
        "house_number": house_number_classes
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse the input JSON
        data = request.json
        violation_type_code = data.get('violation_type_code').strip().upper()
        street = data.get('street').strip().upper()
        boro = data.get('boro').strip().upper()
        house_number = data.get('house_number').strip().upper()
        block = data.get('block').strip().upper()  # Make sure 'block' or missing feature is added

        # Encode the input values
        violation_type_code_encoded = violation_type_code_classes.index(violation_type_code)
        street_encoded = street_classes.index(street)
        boro_encoded = boro_classes.index(boro)
        house_number_encoded = house_number_classes.index(house_number)

        # Prepare the input features (Ensure you pass all 5 features)
        features = np.array([[violation_type_code_encoded, street_encoded, boro_encoded, house_number_encoded, int(block)]], dtype=np.float64)

        # Scale the input features using the saved scaler
        features_scaled = scaler.transform(features)

        # Make the prediction
        prediction = model.predict(features_scaled)
        predicted_category_index = np.argmax(prediction[0])

        # Map the predicted index back to the violation category
        predicted_category = violation_category_classes[predicted_category_index]

        return jsonify({'violation_category': predicted_category})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
