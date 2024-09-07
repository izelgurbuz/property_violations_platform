import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import os

# Step 1: Load the dataset
url = "https://data.cityofnewyork.us/resource/3h2n-5cm9.csv?$limit=50000"
data = pd.read_csv(url)

# Debug: Print initial dataset shape
print(f"Initial dataset shape: {data.shape}")

# Step 2: Data Cleaning and Preparation
# Keep only necessary columns and drop rows with missing values
# Ensure you consistently use the same features during training and prediction
data = data[['violation_type_code', 'street', 'boro', 'block', 'house_number', 'violation_category']].dropna()


# Debug: Print dataset shape after dropping missing values
print(f"Dataset shape after dropping missing values: {data.shape}")

# Step 3: Encode Categorical Variables using LabelEncoder
# Encode violation_type_code
violation_type_code_encoder = LabelEncoder()
data['violation_type_code'] = violation_type_code_encoder.fit_transform(data['violation_type_code'])

# Encode street
street_encoder = LabelEncoder()
data['street'] = street_encoder.fit_transform(data['street'])

# Encode boro
boro_encoder = LabelEncoder()
data['boro'] = boro_encoder.fit_transform(data['boro'])

# Encode house_number (optional: can treat it as a categorical variable or a numeric feature)
house_number_encoder = LabelEncoder()
data['house_number'] = house_number_encoder.fit_transform(data['house_number'])

# Encode violation_category
category_encoder = LabelEncoder()
data['violation_category'] = category_encoder.fit_transform(data['violation_category'])

# Debug: Check unique values after encoding
print(f"Encoded values in 'violation_type_code': {np.unique(data['violation_type_code'])}")
print(f"Encoded values in 'street': {np.unique(data['street'])}")
print(f"Encoded values in 'boro': {np.unique(data['boro'])}")
print(f"Encoded values in 'house_number': {np.unique(data['house_number'])}")

# Step 4: Preprocessing the Data
X = data.drop(columns=['violation_category'])
y = data['violation_category']

# Debug: Check the shape of X and y before scaling
print(f"X shape: {X.shape}, y shape: {y.shape}")

# Step 5: Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Debug: Print mean and std of scaled features
print(f"Mean of scaled features: {X_scaled.mean(axis=0)}")
print(f"Std of scaled features: {X_scaled.std(axis=0)}")

# Ensure the models directory exists
if not os.path.exists('models'):
    os.makedirs('models')

# Save the scaler for later use
joblib.dump(scaler, 'models/scaler.pkl')

# Step 6: Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 7: Save Preprocessed Data
np.savez('data/processed_data.npz', X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

# Step 8: Save Encoders (mappings) to JSON
encoders = {
    'violation_type_code': list(map(str, violation_type_code_encoder.classes_)),
    'street': list(map(str, street_encoder.classes_)),
    'boro': list(map(str, boro_encoder.classes_)),
    'house_number': list(map(str, house_number_encoder.classes_)),
    'violation_category': list(map(str, category_encoder.classes_))
}

# Ensure encoders are Python-friendly (convert int64 to int if needed)
encoders_clean = {k: [int(e) if isinstance(e, np.int64) else e for e in v] for k, v in encoders.items()}

with open('data/mappings.json', 'w') as f:
    json.dump(encoders_clean, f)
