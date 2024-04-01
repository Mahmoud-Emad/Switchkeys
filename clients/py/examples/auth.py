"""
SwitchKey Auth Example

This script demonstrates how to use the SwitchKey client for user authentication.

Usage:
1. Import the necessary modules:
    ```python
    from switchkey.api.request.types import UserTypeEnum
    from switchkey.core.base import SwitchKey
    ```

2. Initialize a SwitchKey instance:
    ```python
    switch_key = SwitchKey()
    ```

3. Use the `register` method to register a new user in the SwitchKey project and save the access/refresh tokens in a `config.ini` file to be used for further interactions in the project:
    ```python
    user = switch_key.auth.register(
        email="Mahmoud_Emad@gmail.com",
        first_name="Mahmoud",
        last_name="Emad",
        password="8080",
        user_type=UserTypeEnum.ADMINISTRATOR.value
    )
    ```

4. Retrieve the access token for further use:
    ```python
    SWITCH_KEY_API_TOKEN = user.access_token
    print("Access Token:", SWITCH_KEY_API_TOKEN)
    ```

Note:
- Replace the email, first name, last name, and password values with your desired user credentials.
- By default, the created user will have ADMINISTRATOR privileges, but you can change it to have USER privileges by using `UserTypeEnum.USER.value`.
- Make sure to handle exceptions and errors appropriately in a production environment.

"""

from switchkey.api.request.types import UserTypeEnum
from switchkey.core.base import SwitchKey

# Initialize SwitchKey instance
switch_key = SwitchKey()

# Register a new user
user = switch_key.auth.register(
    email="Mahmoud_Emad@gmail.com",
    first_name="Mahmoud",
    last_name="Emad",
    password="8080",
    user_type=UserTypeEnum.ADMINISTRATOR.value
)

# Retrieve the access token
SWITCH_KEY_API_TOKEN = user.access_token
print("Access Token:", SWITCH_KEY_API_TOKEN)
