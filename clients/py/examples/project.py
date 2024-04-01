"""
SwitchKeys Project Example

This script demonstrates how to use the SwitchKeys client for managing projects.

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

3. Create an organization using the `create` method:
    ```python
    organization = switch_key.organization.create(name="Threefold")
    ```

4. Create a project on the created organization using the `create` method:
    ```python
    project = switch_key.organization.projects.create(name="TFGrid TS", organization_id=organization.id)
    print("Project ID:", project.id)
    print("Organization Name:", project.organization.name)
    ```

5. Update an existing project using the `update` method:
    ```python
    project = switch_key.organization.projects.update(new_name="TFGrid TS", project_id=8, new_organization_id=6)
    print("Updated Project Name:", project.name)
    ```

6. Get information about a specific project using the `get` method:
    ```python
    project = switch_key.project.get(project_id=8)
    print("Project Details:", project)
    ```

7. Delete a project using the `delete` method:
    ```python
    project = switch_key.project.delete(project_id=8)
    print("Deleted Project:", project)
    ```

Note:
- Replace "your_api_token_here" with your actual API token.
- Ensure to handle exceptions and errors appropriately in a production environment.
"""

from switchkeys.core.base import SwitchKeys

# Initialize SwitchKeys instance with the provided API token
SWITCH_KEY_API_TOKEN = "your_api_token_here"
switch_key = SwitchKeys(api_token=SWITCH_KEY_API_TOKEN)

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
# project = switch_key.project.delete(project_id=8)
# print("project: ", project)
