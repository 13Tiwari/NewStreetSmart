import pandas as pd
import joblib

# Load the saved model
model = joblib.load('Backend/Data/Model/crime_model.pkl')

# Load the data
data = pd.read_csv('Backend/Data/CleanedData/cleaned_crime_data.csv')

# Predict clusters for the data
data['cluster'] = model.predict(data[['latitude', 'longitude']])

# Prepare data for visualization
clustered_data = data[['latitude', 'longitude', 'cluster']]

print(clustered_data.head())