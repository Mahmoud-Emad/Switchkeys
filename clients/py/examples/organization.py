# Import the SwitchKey module
from switchkey.core.base import SwitchKey

SWITCH_KEY_API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExOTI3MzY0LCJpYXQiOjE3MTE5MTgwNjQsImp0aSI6ImUzMTFjZWU2OWM5MzQ1ZTVhNTAzOTQxZDllMTEwMTVhIiwidXNlcl9pZCI6MX0.BOfPO7MY1SsFl7IIM9BwxueWdvpxFk1jF5lX4rpZeMQ"

# Initialize SwitchKey instance with the provided API token
switch_key = SwitchKey(api_token=SWITCH_KEY_API_TOKEN)

# To create an organization, provide its name as a parameter.
# The response will be a SwitchKeyOrganizationResponseType object or an error if there's an issue.

# organization = switch_key.organization.create(name="Threefold")

# Get an organization by its ID
# organization = switch_key.organization.get(organization_id=13)

# Update an organization by its ID
# organization = switch_key.organization.update(organization_id=14, new_name="Threefold3", new_members=[]) # 1 is the member ID.

# Delete an organization by its ID
# organization = switch_key.organization.delete(organization_id=15) # Will return 'Deleted' if the organization is deleted; otherwise, an error message.

# Access organization data using its properties.
# organization_name = organization.name  # Retrieves the organization name (e.g., "Threefold")
# organization_id = organization.id  # Retrieves the unique identifier for the organization
# organization_members = organization.members  # Retrieves the members of the organization (empty if not specified during creation)
# organization_owner = organization.owner  # Retrieves the owner of the organization

# Example usage of organization data:
# print("organization_name", organization_name)
# print("organization_id", organization_id)
# print("organization_members", organization_members)
# print("organization_owner", organization_owner)
# print("organization_owner email", organization_owner.email)
