from azureml.core import Workspace, Model, Environment
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.model import InferenceConfig

# Connect to Azure ML workspace
ws = Workspace.from_config()

# Register the model
model = Model.register(workspace=ws, model_name='crime_model', model_path='Backend/Data/Model/crime_model.pkl')

# Define the environment
env = Environment.from_conda_specification(name='sklearn-env', file_path='Backend/Azure/environment.yml')

# Create an inference configuration
inference_config = InferenceConfig(entry_script='Backend/score.py', environment=env)

# Define the deployment configuration
aci_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

# Deploy the model
service = Model.deploy(workspace=ws,
                       name='crime-density-service-1',
                       models=[model],
                       inference_config=inference_config,
                       deployment_config=aci_config)
service.wait_for_deployment(show_output=True)

print(f"Scoring URI: {service.scoring_uri}")