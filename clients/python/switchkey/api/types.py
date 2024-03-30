from typing import Dict, Any, List
from uuid import UUID

from switchkey.api.request import SwitchKeyRequest, SwitchKeyRequestMethod
from switchkey.api.routes import EndPoints, SwitchKeyRoutes


class SwitchKeyFeatureType:
    """
    Represents features associated with the SwitchKey.

    Attributes:
        __features (Dict[str, Any]): A dictionary containing the user's features.

    Methods:
        has(feature: str) -> bool: Check if the user has the feature.
        get(feature: str) -> Any: Get the value of a feature.
        create(feature: str, value: str) -> None: Create a new feature with a value.
        is_enabled(feature: str) -> bool: Check if a feature is enabled.
        value_of(key: str) -> Any: Retrieve the value of the specified feature key.
    """

    def __init__(self, features: Dict[str, Any], environment_key: UUID, user_id: int):
        """
        Initialize the SwitchKeyFeatureType object.

        Args:
            features (Dict[str, Any]): A dictionary containing the user's features.
            environment_key (UUID): The environment key to load the environment.
        """

        self.__features = features
        self.environment_key = environment_key
        self.__routes = SwitchKeyRoutes()
        self.user_id = user_id

    def has(self, feature: str) -> bool:
        """Check if a feature is enabled."""
        return feature in self.__features

    def get(self, feature: str) -> Any:
        """Get the value of a feature."""
        return self.__features.get(feature)

    def set(self, feature: str, value: Any) -> None:
        """
        Create/Update a feature with a value.

        Args:
            feature (str): The name of the feature to create/update.
            value (Any): The value to assign to the feature.

        Raises:
            ValueError: If the feature name is empty or None, or if the value is None.

        Example:
            ``feature_type = SwitchKeyFeatureType(features={'debug': False})``\n
            ``feature_type.set('debug', True)``
        """
        # Validate input parameters
        if not feature:
            raise ValueError("Feature name cannot be empty.")
        if value is None:
            raise ValueError("Feature value cannot be None. Set it to False instead.")

        # Make API call to set the feature
        response = SwitchKeyRequest.call(
            self.__routes.get_route(EndPoints.ENVIRONMENTS_SET, self.environment_key, self.user_id),
            SwitchKeyRequestMethod.POST,
            data={"key": feature, "value": str(value).lower() if type(value) == bool else value},
        )

        # Check response status and update features if successful
        if response.get_status_code() == 200:
            self.__features = response.get_data()
        else:
            print("Failed to set feature:", response.get_error_message())

    def is_enabled(self, feature: str) -> bool:
        """Check if a feature is enabled."""
        if feature in self.__features:
            return bool(self.__features[feature].get("is_enabled"))
        raise KeyError(f"'{feature}' does not exist in the user features.")

    def value_of(self, feature: str) -> Any:
        """
        Retrieve the value of the specified feature key.

        Args:
            key (str): The key of the feature whose value needs to be retrieved.

        Returns:
            Any: The value associated with the provided key.

        Raises:
            KeyError: If the specified feature does not exist in the user's features.
        """
        if feature in self.__features:
            return self.__features[feature].get("value")
        raise KeyError(f"'{feature}' does not exist in the user features.")


class SwitchKeyDeviceType:
    """
    Represents a Type object for device information.
    It's not serialized yet.
    """

    def __init__(self):
        pass


class SwitchKeyProjectUserType:
    """
    Represents a Type object for project users.

    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username of the user.
        device (SwitchKeyDeviceType): The device information of the user.
        features (SwitchKeyFeatureType): The features associated with the user.
        environment_key (uuid): The key of the environment, to access the API.
    Methods:
        N/A
    """

    def __init__(
        self,
        id: int,
        username: str,
        device: SwitchKeyDeviceType,
        features: Dict[str, Any],
        environment_key: UUID,
    ):
        self.id = id
        self.username = username
        self.device = device
        self.features = SwitchKeyFeatureType(
            features=features, environment_key=environment_key, user_id=self.id
        )


class SwitchKeyUserType:
    """
    Represents a Type object for users.

    Attributes:
        id (int): The unique identifier of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        full_name (str): The full name of the user.
        email (str): The email address of the user.
        joining_at (str): The date/time when the user joined.
        background_color (str): The background color associated with the user.
        is_active (bool): Indicates whether the user is active.

    Methods:
        N/A
    """

    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        full_name: str,
        email: str,
        joining_at: str,
        background_color: str,
        is_active: bool,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.joining_at = joining_at
        self.background_color = background_color
        self.is_active = is_active


class SwitchKeyOrganizationType:
    """
    Represents a Type object for organizations.

    Attributes:
        id (int): The unique identifier of the organization.
        name (str): The name of the organization.
        owner (SwitchKeyUserType): The owner of the organization.
        members (List[SwitchKeyUserType]): The members of the organization.
        created (str): The date/time when the organization was created.
        modified (str): The date/time when the organization was last modified.

    Methods:
        N/A
    """

    def __init__(
        self,
        id: int,
        name: str,
        owner: SwitchKeyUserType,
        members: List[SwitchKeyUserType],
        created: str,
        modified: str,
    ):
        self.id = id
        self.name = name
        self.owner = owner
        self.members = members
        self.created = created
        self.modified = modified


class SwitchKeyProjectType:
    """
    Represents a Type object for projects.

    Attributes:
        id (int): The unique identifier of the project.
        name (str): The name of the project.
        organization (SwitchKeyOrganizationType): The organization to which the project belongs.
        created (str): The date/time when the project was created.
        modified (str): The date/time when the project was last modified.

    Methods:
        N/A
    """

    def __init__(
        self,
        id: int,
        name: str,
        created: str,
        modified: str,
        organization: SwitchKeyOrganizationType,
    ):
        self.id = id
        self.name = name
        self.organization = organization
        self.created = created
        self.modified = modified


class SwitchKeyEnvironmentType:
    """
    Represents a Type object for environments.

    Attributes:
        id (int): The unique identifier of the environment.
        name (str): The name of the environment.
        project (SwitchKeyProjectType): The project associated with the environment.
        environment_key (str): The key of the environment.
        created (str): The date/time when the environment was created.
        modified (str): The date/time when the environment was last modified.
        users (List[SwitchKeyProjectUserType]): The users associated with the environment.

    Methods:
        N/A
    """

    def __init__(
        self,
        id: int,
        name: str,
        created: str,
        modified: str,
        project: SwitchKeyProjectType,
        environment_key: str,
        users: List[SwitchKeyProjectUserType],
    ):
        self.id = id
        self.name = name
        self.project = project
        self.environment_key = environment_key
        self.created = created
        self.modified = modified
        self.users = users

    def get_user(self, username: str):
        for user in self.users:
            if user.username.lower() == username.lower():
                return user
        return None
