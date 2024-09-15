from flask import Flask, jsonify
import pandas as pd
from sklearn.cluster import KMeans
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Welcome to the Cluster Data API"

@app.route('/api/cluster-data', methods=['GET'])
def get_cluster_data():
    # Load preprocessed data
    data = pd.read_csv('Backend/Data/CleanedData/cleaned_crime_data.csv')

    # Load the trained model
    model = joblib.load('Backend/Data/Model/crime_model.pkl')

    # Predict clusters
    data['cluster'] = model.predict(data[['latitude', 'longitude']])

    # Calculate the size of each cluster
    cluster_sizes = data['cluster'].value_counts().to_dict()

    # Calculate the centroid of each cluster
    cluster_centroids = model.cluster_centers_

    # Prepare cluster data for the frontend
    cluster_data = []
    for cluster_id, size in cluster_sizes.items():
        # print("CLUSTER ID: ", cluster_id)
        centroid = cluster_centroids[cluster_id]
        cluster_data.append({
            'lat': float(centroid[0]),
            'lng': float(centroid[1]),
            'size': int(size)
        })
    #print("CLUSTER DATA\n", cluster_data)
    return jsonify({"clusters": cluster_data})

if __name__ == '__main__':
    app.run(debug=True)