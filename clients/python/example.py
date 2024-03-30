# Usage Example
# Import the SwitchKey module
from switchkey.core.base import SwitchKey

# Initialize SwitchKey instance with the environment key
switch_key = SwitchKey(environment_key="1931ca88-f3d8-4aac-8019-a45e78f38d19")

# Connect to the environment to load all its data
switch_key.connect()

# Load users based on their username or id
hamada_user = switch_key.environment.get_user("hamada") # -> user or None
thunder_user = switch_key.environment.get_user("thunder") # -> user or None

if hamada_user is not None and thunder_user is not None:
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