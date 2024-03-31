# Import the SwitchKey module
from switchkey.core.base import SwitchKey


class ProjectExample:
  
  def __init__(self):
    SWITCH_KEY_API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExOTI3MzY0LCJpYXQiOjE3MTE5MTgwNjQsImp0aSI6ImUzMTFjZWU2OWM5MzQ1ZTVhNTAzOTQxZDllMTEwMTVhIiwidXNlcl9pZCI6MX0.BOfPO7MY1SsFl7IIM9BwxueWdvpxFk1jF5lX4rpZeMQ"

    # Initialize SwitchKey instance with the provided API token
    switch_key = SwitchKey(api_token=SWITCH_KEY_API_TOKEN)

    # Create an organization
    organization = switch_key.organization.create(name="Threefold")

    # Create a project on the created organization
    project = switch_key.organization.projects.create(name="TFGrid TS", organization_id=organization.id)
    print(project.id) # Check the created project ID.
    print(project.organization.name) # Check the created project organization name.
