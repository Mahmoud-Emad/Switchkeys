# Import the SwitchKey module
from switchkey.core.base import SwitchKey

# Initialize SwitchKey instance with the environment key
switch_key = SwitchKey(environment_key="1931ca88-f3d8-4aac-8019-a45e78f38d19")

# Connect to the environment to load all its data
switch_key.connect()

# Getters
# Load users based on their username or id
hamada_user = switch_key.environment.get_user("hamada")  # Retrieve user by username
thunder_user = switch_key.environment.get_user("thunder")  # Retrieve user by username

if hamada_user and thunder_user:
    # Accessing user features
    hamada_features = hamada_user.features
    thunder_features = thunder_user.features

    # Access specific features of a user
    print(f"Debug feature value for user 'hamada': {hamada_features.value_of('debug')}")  # => True | False
    print(f"Debug feature value for user 'thunder': {thunder_features.value_of('debug')}")  # => True | False

    # Check if a user has a specific feature
    print(f"Does user 'hamada' have the 'debug' feature?: {hamada_features.has('debug')}")  # => True | False
    print(f"Does user 'thunder' have the 'debug' feature?: {thunder_features.has('debug')}")  # => True | False

    # Check if a feature is enabled for a user
    print(f"Is the 'debug' feature enabled for user 'thunder'?: {thunder_features.is_enabled('debug')}")  # => True | False
    
# Setters
hamada_user = switch_key.environment.get_user("hamada")
if hamada_user:
    # Set a new feature for the user
    hamada_user.features.set("debug22", True)
    print(f"Value of 'debug22' feature for user 'hamada': {hamada_user.features.value_of('debug22')}")  # => True
    print(f"Is the 'debug22' feature enabled for user 'hamada'?: {hamada_user.features.is_enabled('debug22')}")  # => True, because new features are enabled by default
