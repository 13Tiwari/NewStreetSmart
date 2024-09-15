from azureml.core import Workspace, Webservice

# Connect to Azure ML workspace
ws = Workspace.from_config()

# Delete the existing service
existing_service = Webservice(name='crime-density-service', workspace=ws)
existing_service.delete()