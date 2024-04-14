"""
SwitchKeys Organization Example

This script demonstrates how to use the SwitchKeys client for managing organizations.

Usage:
1. Import the SwitchKeys module:
    ```python
    from switchkeys.core.base import SwitchKeys
    ```

2. Initialize a SwitchKeys instance with the provided API token:
    ```python
    SWITCH_KEY_API_TOKEN = "your_api_token_here"
    switch_key = SwitchKeys(api_token=SWITCH_KEY_API_TOKEN)
    ```

3. To create an organization, provide its name as a parameter to the `create` method:
    ```python
    organization = switch_key.organization.create(name="Threefold")
    ```

4. Retrieve an organization by its ID using the `get` method:
    ```python
    organization = switch_key.organization.get(organization_id=13)
    ```

5. Update an organization by its ID using the `update` method:
    ```python
    organization = switch_key.organization.update(organization_id=14, new_name="Threefold3", new_members=[])
    ```

6. Delete an organization by its ID using the `delete` method:
    ```python
    organization = switch_key.organization.delete(organization_id=15)
    ```

7. Access organization data using its properties:
    ```python
    organization_name = organization.name
    organization_id = organization.id
    organization_members = organization.members
    organization_owner = organization.owner
    ```

8. Example usage of organization data:
    ```python
    print("organization_name:", organization_name)
    print("organization_id:", organization_id)
    print("organization_members:", organization_members)
    print("organization_owner:", organization_owner)
    print("organization_owner email:", organization_owner.email)
    ```

Note:
- Replace "your_api_token_here" with your actual API token.
- Ensure to handle exceptions and errors appropriately in a production environment.

"""

from switchkeys.core.base import SwitchKeys

# Initialize SwitchKeys instance with the provided API token
SWITCH_KEY_API_TOKEN = "your_api_token_here"
switch_key = SwitchKeys(api_token=SWITCH_KEY_API_TOKEN)

# To create an organization, provide its name as a parameter.
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
# print("organization_name:", organization_name)
# print("organization_id:", organization_id)
# print("organization_members:", organization_members)
# print("organization_owner:", organization_owner)
# print("organization_owner email:", organization_owner.email)
