# train.py
import pandas as pd
from sklearn.cluster import KMeans
from azureml.core import Run
import joblib

# Load preprocessed data
data = pd.read_csv('Backend/Data/CleanedData/cleaned_crime_data.csv')

# Train a KMeans clustering model
model = KMeans(n_clusters=50)
model.fit(data[['latitude', 'longitude']])

# Save the model
joblib.dump(model, 'crime_model.pkl')

