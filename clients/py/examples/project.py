# Import the SwitchKey module
from switchkey.core.base import SwitchKey


class ProjectExample:
  
  def __init__(self):
    SWITCH_KEY_API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExOTM2NzE3LCJpYXQiOjE3MTE5Mjc0MTcsImp0aSI6ImY1NmY0YmVkNWEwNDRlOTM4NDU3NWU0Y2E1N2Y0NTBhIiwidXNlcl9pZCI6MX0.EPvw6F35d2sk1b0Mn3Mmta0bKxqeHrEkGqJ0cH9pxn4"

    # Initialize SwitchKey instance with the provided API token
    switch_key = SwitchKey(api_token=SWITCH_KEY_API_TOKEN)

    # Create an organization
    # organization = switch_key.organization.create(name="Threefold")

    # Create a project on the created organization
    # project = switch_key.organization.projects.create(name="TFGrid TS", organization_id=organization.id)
    # print(project.id) # Check the created project ID.
    # print(project.organization.name) # Check the created project organization name.

    # Update an exact project, now we're going to change the organization.
    # project = switch_key.organization.projects.update(new_name="TFGrid TS", project_id=8, new_organization_id=6)
    # print("Updated: ", project.name)
    
    # Get an exact project.
    # project = switch_key.project.get(project_id=8)
    # print("project: ", project)

    # Delete an exact project.
    project = switch_key.project.delete(project_id=8)
    print("project: ", project)