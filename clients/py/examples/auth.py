# Import the SwitchKey module
from switchkey.api.request.types import UserTypeEnum
from switchkey.core.base import SwitchKey

class AuthExample:

  def __init__(self):
    SWITCH_KEY_API_TOKEN = ""

    # Initialize SwitchKey instance with the provided API token
    switch_key = SwitchKey(api_token=SWITCH_KEY_API_TOKEN)
    user = switch_key.auth.register(
      email="Mahmoud_Emad@gmail.com",
      first_name="Mahmoud",
      last_name="Emad",
      password="8080",
      user_type=UserTypeEnum.ADMINISTRATOR.value # The created user wil be an ADMINISTRATOR by defualt, you can change it to be just `user` with user privileges.
    )
    
    SWITCH_KEY_API_TOKEN = user.access_token 
    print("Access Token", SWITCH_KEY_API_TOKEN)
    
