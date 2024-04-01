# SwitchKey Auth Example

This example demonstrates how to use the SwitchKey client for user authentication.

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
    print("Access Token", SWITCH_KEY_API_TOKEN)
    ```

Attributes:
    None

Methods:
    None
