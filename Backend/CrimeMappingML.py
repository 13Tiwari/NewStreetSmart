import pandas as pd 
from DataCleaner import clean_data
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment
from azureml.core import Run
from sklearn.cluster import KMeans
import joblib

#Uncomment to clean additional data
#clean_data('crime_data.csv')

ws = Workspace.from_config(path='config.json')
#print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')

# Create an experiment
experiment = Experiment(workspace=ws, name='crime-density-clustering')

# Create a script run configuration
env = Environment.from_conda_specification(name='sklearn-env', file_path='Backend/Azure/environment.yml')
src = ScriptRunConfig(source_directory='Backend', script='train.py', compute_target='cpu-cluster', environment=env)

# Submit the experiment
run = experiment.submit(src)
run.wait_for_completion(show_output=True)
print("works")