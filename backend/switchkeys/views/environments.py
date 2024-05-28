"""
This module contains API views for managing project environments and related features.

Endpoints:
- `ProjectEnvironmentKeyApiView`: Retrieves an environment by its key, also can delete it.
- `BaseProjectEnvironmentApiView`: Lists and creates project environments.
- `ProjectEnvironmentApiView`: Retrieves, updates, and deletes project environments.
- `AddEnvironmentUserAPIView`: Adds a user to an environment.
- `EnvironmentUserFeaturesApiView`: Retrieves user features from an environment.
- `DeleteEnvironmentUserFeature`: Deletes a user feature on an environment.
- `SetEnvironmentUserFeaturesApiView`: Sets user feature on an environment.
- `RemoveEnvironmentUserAPIView`: Removes a user from an environment.
- `BaseEnvironmentFeatureAPIView`: Lists and creates environment features.
- `DeleteEnvironmentFeatureAPIView`: Deletes an environment feature.
- `UpdateEnvironmentFeatureAPIView`: Updates an environment feature.
"""

from uuid import UUID
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.request import Request
from switchkeys.api.permissions import IsAdminUser, UserIsAuthenticated
from switchkeys.utils.validators import is_valid_uuid
from switchkeys.models.environments import (
    EnvironmentFeature,
    SwitchKeysFeature,
    UserFeature,
)
from switchkeys.models.users import DeviceType
from switchkeys.utils.wrappers import unique_field_error, value_not_accepted_error
from switchkeys.services.projects import get_project_by_id
from switchkeys.models.management import OrganizationProject
from switchkeys.api.custom_response import CustomResponse
from switchkeys.services.environments import (
    create_environment_user,
    get_all_environment_features,
    get_all_environments,
    get_environment_by_id,
    get_environment_by_key,
    get_environment_feature,
    get_environment_user_username,
    is_feature_created,
    validate_unique_environment_name,
)
from switchkeys.serializers.environments import (
    AddEnvironmentUserSerializer,
    EnvironmentFeatureSerialize,
    ProjectEnvironmentSerializer,
    RemoveEnvironmentUserSerializer,
    SwitchKeysFeatureSerializer,
    EnvironmentFeatureSerializer,
    UserFeatureSerializers,
)


class ProjectEnvironmentKeyApiView(ListAPIView):
    """
    API endpoint for retrieving an environment by its key.
    """

    serializer_class = ProjectEnvironmentSerializer

    def get(self, request: Request, environment_key: UUID):
        """Get the queryset of projects for the specified organization"""
        environment_key = self.kwargs.get("environment_key")

        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not valid UUID."
            )

        environment = get_environment_by_key(environment_key)

        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        return CustomResponse.success(
            message="Environment found.",
            data=self.serializer_class(environment).data,
        )

    def delete(self, request: Request, environment_key: UUID):
        """Delete an environment by it's key."""
        environment_key = self.kwargs.get("environment_key")

        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not valid UUID."
            )

        environment = get_environment_by_key(environment_key)

        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        project: OrganizationProject = environment.project
        if request.user.id != project.organization.owner.id:
            return CustomResponse.unauthorized(
                message="You do not have permission to access this resource because you are not the creator of the organization that owns this project."
            )

        environment.delete()
        return CustomResponse.success(
            message="Project has been updated successfully.",
            status_code=204,
        )


class BaseProjectEnvironmentApiView(ListAPIView):
    """
    API endpoint for listing and creating project environments.
    """

    serializer_class = ProjectEnvironmentSerializer
    permission_classes = []

    def get_permissions(self):
        """
        Sets permissions for the view based on request method.
        """
        if self.request.method == "GET":
            self.permission_classes = []
        else:
            self.permission_classes = [IsAdminUser]

        return super(BaseProjectEnvironmentApiView, self).get_permissions()

    def get_queryset(self) -> CustomResponse:
        """
        Retrieves all environments in the system.
        """
        get_queryset = get_all_environments()
        return get_queryset

    def post(self, request: Request) -> CustomResponse:
        """
        Creates a new project environment.
        """
        environment = request.data
        serializer = self.get_serializer(data=environment)
        if serializer.is_valid():
            project_id: int = serializer.validated_data.get("project_id")
            project: OrganizationProject = get_project_by_id(str(project_id))

            if project is None:
                return CustomResponse.not_found(message="Project not found.")

            if request.user.id != project.organization.owner.id:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not the creator of the organization that owns this project."
                )

            environment_name: str = serializer.validated_data.get("name")
            is_environment_exist = validate_unique_environment_name(
                environment_name, project
            )

            if is_environment_exist:
                return CustomResponse.bad_request(
                    error=unique_field_error("name"),
                    message=f"It seems you've already created a '{environment_name}' environment for this project. Please remove the existing one before creating a new one, or consider changing the name to avoid duplication.",
                )

            serializer.save(project=project)
            return CustomResponse.success(
                data=serializer.data,
                message="Project environment has been created successfully.",
            )

        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
            data=request.data,
        )


class ProjectEnvironmentApiView(GenericAPIView):
    """
    API endpoint for retrieving, updating, and deleting project environments.
    """

    serializer_class = ProjectEnvironmentSerializer
    permission_classes = []

    def get_permissions(self):
        """
        Sets permissions for the view based on request method.
        """
        if self.request.method == "GET":
            self.permission_classes = []
        else:
            self.permission_classes = [IsAdminUser]

        return super(ProjectEnvironmentApiView, self).get_permissions()

    def get(self, request: Request, environment_id: str) -> CustomResponse:
        """
        Retrieves a project environment by its ID.
        """
        environment = get_environment_by_id(environment_id)

        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )
        return CustomResponse.success(
            data=ProjectEnvironmentSerializer(environment).data,
            message="The project environment found.",
        )

    def put(self, request: Request, environment_id: str) -> CustomResponse:
        """
        Updates a project environment by its ID.
        """
        environment = get_environment_by_id(environment_id)

        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        data = request.data
        serializer = self.get_serializer(environment, data=data)
        if serializer.is_valid():
            project_id: int = serializer.validated_data.get("project_id")
            project: OrganizationProject = get_project_by_id(str(project_id))

            if project is None:
                return CustomResponse.not_found(message="Project not found.")

            if request.user.id != project.organization.owner.id:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not the creator of the organization that owns this project."
                )

            environment_name: str = serializer.validated_data.get("name")
            is_environment_exist = validate_unique_environment_name(
                environment_name, project
            )

            if is_environment_exist:
                return CustomResponse.bad_request(
                    error=unique_field_error("name"),
                    message=f"It seems you've already created a '{environment_name}' environment for this project. Please remove the existing one before creating a new one, or consider changing the name to avoid duplication.",
                )

            serializer.save()
            return CustomResponse.success(
                data=serializer.data,
                message="Organization project environment has been updated successfully.",
                status_code=201,
            )

        return CustomResponse.bad_request(
            data=ProjectEnvironmentSerializer(environment).data,
            message="Please make sure that you entered a valid data..",
            error=serializer.errors,
        )

    def delete(self, request: Request, environment_id: str) -> CustomResponse:
        """
        Deletes a project environment by its ID.
        """
        environment = get_environment_by_id(environment_id)

        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        project: OrganizationProject = environment.project
        if request.user.id != project.organization.owner.id:
            return CustomResponse.unauthorized(
                message="You do not have permission to access this resource because you are not the creator of the organization that owns this project."
            )

        environment.delete()
        return CustomResponse.success(
            message="Project has been updated successfully.",
            status_code=204,
        )


class AddEnvironmentUserAPIView(GenericAPIView):
    """
    API endpoint for adding a user to an environment.
    """

    serializer_class = AddEnvironmentUserSerializer

    def put(self, request: Request, environment_key: UUID) -> CustomResponse:
        """
        Adds a user to the specified environment.
        """

        # Validate environment key
        environment_key = self.kwargs.get("environment_key")
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not a valid UUID."
            )

        environment = get_environment_by_key(environment_key)
        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            user = get_environment_user_username(username)
            if user is None:
                device_data = serializer.validated_data.get("device")
                device_type = device_data.get("device_type")
                device_version = device_data.get("version")
                valid_types = [
                    str(DeviceType.ANDROID).lower(),
                    str(DeviceType.IPHONE).lower(),
                ]

                if device_type not in valid_types:
                    hint = f"Only {', '.join(valid_types)} are allowed."
                    return CustomResponse.bad_request(
                        message=f"You have sent an invalid device type. {hint}",
                        error=value_not_accepted_error(
                            "device_type", device_type, hint
                        ),
                    )

                user = create_environment_user(
                    username=username,
                    device_type=device_type,
                    device_version=device_version,
                )

            environment.users.add(user)
            environment_features = EnvironmentFeature.objects.get_or_create(
                environment=environment
            )[0]

            for feature in environment_features.features.all():
                switchkey_feature = SwitchKeysFeature.objects.get(id=feature.id)
                created = UserFeature.objects.filter(
                    user=user,
                    feature=switchkey_feature,
                )

                if len(created) == 0:
                    UserFeature.objects.create(
                        user=user,
                        feature=switchkey_feature,
                        feature_value=feature.value,
                    )

            environment.save()
            return CustomResponse.success(
                message="User added successfully.", data=serializer.data
            )
        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
        )


class EnvironmentUserFeaturesApiView(GenericAPIView):
    """
    API endpoint for getting user features from an environment.
    """

    serializer_class = UserFeatureSerializers

    def get_queryset(self):
        """
        Get user features from the specified environment.

        Args:
            request (Request): HTTP request object.
            environment_key (UUID): The key of the environment to remove the user from.
            username (str): the enviroment user username.

        Returns:
            CustomResponse: Response object containing the result of the operation.
        """
        environment_key = self.kwargs.get("environment_key")
        username = self.kwargs.get("username")

        # Validate environment key
        environment_key = self.kwargs.get("environment_key")
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not a valid UUID."
            )

        # Get the environment by key
        environment = get_environment_by_key(environment_key)
        if environment is None:
            # Return 404 if the environment does not exist
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        # Get the user from the environment by username
        user = get_environment_user_username(username)
        if user is None:
            # Return 404 if the user does not exist
            return CustomResponse.not_found(message="User not found.")

        if user not in environment.users.all():
            return CustomResponse.bad_request(
                message=f"User `{user.username}` is not on the `{environment.name}` environment, try to add the user first to the environment."
            )

        user_features = UserFeature.objects.filter(user=user)
        return user_features

    def get(
        self, request: Request, environment_key: UUID, username: str
    ) -> CustomResponse:
        """
        Get user features from the specified environment.

        Args:
            request (Request): HTTP request object.
            environment_key (UUID): The key of the environment to remove the user from.
            username (str): the enviroment user username.

        Returns:
            CustomResponse: Response object containing the result of the operation.
        """

        user_features = self.get_queryset()
        return CustomResponse.success(
            message="User features found.",
            data=self.serializer_class(user_features, many=True).data,
        )


class DeleteEnvironmentUserFeature(GenericAPIView):
    """
    API endpoint for deleting user feature on an environment.
    """

    def delete(
        self, request: Request, environment_key: UUID, username: str, feature_name: str
    ):
        """
        Delete user feature on the specified environment.

        Args:
            request (Request): HTTP request object.
            environment_key (UUID): The key of the environment to remove the user from.
            username (str): the enviroment user username.
            feature_name (str): the feature name to be deleted.

        Returns:
            CustomResponse: Response object containing the result of the operation.
        """

        # Validate environment key
        environment_key = self.kwargs.get("environment_key")
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not a valid UUID."
            )

        # Get the environment by key
        environment = get_environment_by_key(environment_key)
        if environment is None:
            # Return 404 if the environment does not exist
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        # Get the user from the environment by username
        user = get_environment_user_username(username)
        if user is None:
            # Return 404 if the user does not exist
            return CustomResponse.not_found(message="User not found.")

        # Validate if the user exist on the environment
        if user not in environment.users.all():
            return CustomResponse.bad_request(
                message=f"User `{user.username}` is not on the `{environment.name}` environment, try to add the user first to the environment."
            )

        # Get and validate the feature, check if the feature exist on the user
        user_features = UserFeature.objects.filter(user=user).filter(
            feature__name=feature_name
        )
        if len(user_features) == 0:
            return CustomResponse.not_found(
                message="Feature not found.",
            )

        user_feature = UserFeature.objects.filter(user=user).get(
            feature__name=feature_name
        )
        user_feature.delete()
        return CustomResponse.success(status_code=204, message="Feature deleted.")


class SetEnvironmentUserFeaturesApiView(GenericAPIView):
    """
    API endpoint for setting user feature on an environment.
    """

    serializer_class = EnvironmentFeatureSerializer

    def put(
        self, request: Request, environment_key: UUID, username: str
    ) -> CustomResponse:
        """
        Set user feature on the specified environment.

        Args:
            request (Request): HTTP request object.
            environment_key (UUID): The key of the environment to remove the user from.
            username (str): the enviroment user username.

        Returns:
            CustomResponse: Response object containing the result of the operation.
        """

        # Validate environment key
        environment_key = self.kwargs.get("environment_key")
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not a valid UUID."
            )

        # Get the environment by key
        environment = get_environment_by_key(environment_key)
        if environment is None:
            # Return 404 if the environment does not exist
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        # Get the user from the environment by username
        user = get_environment_user_username(username)
        if user is None:
            # Return 404 if the user does not exist
            return CustomResponse.not_found(message="User not found.")

        # Validate if the user exist on the environment
        if user not in environment.users.all():
            return CustomResponse.bad_request(
                message=f"User `{user.username}` is not on the `{environment.name}` environment, try to add the user first to the environment."
            )

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse.bad_request(
                message="Please make sure that you entered a valid data.",
                error=serializer.errors,
            )

        feature_name = serializer.validated_data.get("name")
        feature_value = serializer.validated_data.get("value")

        user_features = UserFeature.objects.filter(user=user).filter(
            feature__name=feature_name
        )

        if len(user_features) == 0:
            # Create new user feature
            feature = SwitchKeysFeature.objects.create(
                name=feature_name,
                value=feature_value,
                initial_value=feature_value,
            )

            UserFeature.objects.create(user=user, feature=feature)

        user_feature = UserFeature.objects.filter(user=user).get(
            feature__name=feature_name
        )
        user_feature.feature_value = feature_value
        user_feature.save()

        # Change the value for the user.
        user_feature.feature.value = user_feature.feature_value
        return CustomResponse.success(
            message="User features found.",
            data=SwitchKeysFeatureSerializer(user_feature.feature).data,
        )


class RemoveEnvironmentUserAPIView(GenericAPIView):
    """
    API endpoint for removing a user from an environment.
    """

    serializer_class = RemoveEnvironmentUserSerializer

    def put(self, request: Request, environment_key: UUID) -> CustomResponse:
        """
        Remove a user from the specified environment.

        Args:
            request (Request): HTTP request object.
            environment_key (UUID): The key of the environment to remove the user from.

        Returns:
            CustomResponse: Response object containing the result of the operation.
        """

        # Validate environment key
        environment_key = self.kwargs.get("environment_key")
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not a valid UUID."
            )

        # Get the environment by key
        environment = get_environment_by_key(environment_key)
        if environment is None:
            # Return 404 if the environment does not exist
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        # Validate the incoming data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Get the username from the serializer data
            username = serializer.validated_data.get("username")
            # Get the user from the environment by username
            user = get_environment_user_username(username)
            if user is None:
                # Return 404 if the user does not exist
                return CustomResponse.not_found(message="User not found.")

            # Delete user features associated with the user
            user_features = UserFeature.objects.filter(user=user).all()
            user_features.delete()

            # Remove the user from the environment
            environment.users.remove(user)
            environment.save()

            data = serializer.data
            data["featrues"] = user_features

            return CustomResponse.success(
                message="User removed successfully.", data=data
            )
        # Return 400 if the data is not valid
        return CustomResponse.bad_request(
            message="Please make sure that you entered valid data.",
            error=serializer.errors,
        )


class BaseEnvironmentFeatureAPIView(GenericAPIView):

    serializer_class = EnvironmentFeatureSerialize
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = []
        else:
            self.permission_classes = [UserIsAuthenticated]

        return super(BaseEnvironmentFeatureAPIView, self).get_permissions()

    def get_queryset(self):
        """Get all ``environment features`` in the system."""
        environment_key = self.kwargs.get("environment_key")
        environment = get_environment_by_key(environment_key)
        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not valid UUID."
            )

        get_queryset = get_all_environment_features(environment)
        return get_queryset

    def get(self, request: Request, environment_key: UUID):
        """Get all features exists on the environment"""
        environment = self.get_queryset()
        return CustomResponse.success(
            message="Environment features found.",
            data=self.serializer_class(environment, many=True).data,
        )

    def post(self, request: Request, environment_key: UUID) -> CustomResponse:
        """
        Create a new environment feature.

        Args:
            request (Request): The HTTP request object containing data for creating the feature.
            environment_key (UUID): The UUID of the environment where the feature will be created.

        Returns:
            CustomResponse: Response indicating the result of the feature creation process.
        """

        # Validate environment key
        environment_key = self.kwargs.get("environment_key")
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not a valid UUID."
            )

        # Validate serializer data
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse.bad_request(
                message="Please make sure that you entered valid data.",
                error=serializer.errors,
                data=request.data,
            )

        # Get the environment
        environment = get_environment_by_key(environment_key)
        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        # Extract feature name and value from serializer
        feature_name = serializer.validated_data.get("name")
        feature_value = serializer.validated_data.get("value")

        # Check if the feature with the same name already exists in the environment
        if is_feature_created(feature_name, environment):
            return CustomResponse.bad_request(
                message="The environment already has a feature with the same name.",
                error=unique_field_error("name"),
            )

        # Create the new feature
        feature = SwitchKeysFeature.objects.create(
            name=feature_name,
            value=feature_value,
            initial_value=feature_value,
        )

        # Get and add the feature to the environment
        env_feature = EnvironmentFeature.objects.get(environment=environment)
        env_feature.features.add(feature)
        environment.save()

        # Assign the new feature to all users in the environment
        for user in environment.users.all():
            UserFeature.objects.create(
                user=user, feature=feature, feature_value=feature_value
            )

        return CustomResponse.success(
            data=SwitchKeysFeatureSerializer(feature).data,
            message="Project environment has been created successfully.",
        )


class DeleteEnvironmentFeatureAPIView(GenericAPIView):
    # Update the permission later.
    permission_classes = []

    def delete(self, request: Request, environment_key: UUID, feature_name: str):
        """Delete an environment feature from the environment and from all environment users"""
        # Validate environment key
        environment_key = self.kwargs.get("environment_key")
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not a valid UUID."
            )

        # Get the environment
        environment = get_environment_by_key(environment_key)
        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        # Check if the feature with the same name already exists in the environment
        if not is_feature_created(feature_name, environment):
            return CustomResponse.not_found(
                message=f"Feature '{feature_name}' does not exist on the '{environment.name}' environment.",
            )

        env_feature = get_environment_feature(feature_name, environment)
        feature = env_feature.features.get(name=feature_name)
        feature.delete()

        return CustomResponse.success(
            status_code=204,
            message="The environment feature has been deleted successfully.",
        )


class UpdateEnvironmentFeatureAPIView(GenericAPIView):
    serializer_class = EnvironmentFeatureSerializer
    # Update the permission later.
    permission_classes = []

    def put(self, request: Request, environment_key: UUID, feature_name: str):
        """Update an environment feature"""
        # Validate environment key
        environment_key = self.kwargs.get("environment_key")
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not a valid UUID."
            )

        # Get the environment
        environment = get_environment_by_key(environment_key)
        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        # Check if the feature with the same name already exists in the environment
        if not is_feature_created(feature_name, environment):
            return CustomResponse.not_found(
                message=f"Feature '{feature_name}' does not exist on the '{environment.name}' environment.",
            )

        env_feature = get_environment_feature(feature_name, environment)
        feature = env_feature.features.get(name=feature_name)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse.bad_request(
                message="Please make sure that you entered valid data.",
                error=serializer.errors,
                data=request.data,
            )

        # Extract feature name and value from serializer
        new_feature_name = serializer.validated_data.get("name")
        new_feature_value = serializer.validated_data.get("value")

        # Check if the feature with the same name already exists in the environment
        if new_feature_name != feature_name and is_feature_created(
            new_feature_name, environment
        ):
            return CustomResponse.bad_request(
                message="The environment already has a feature with the same name.",
                error=unique_field_error("name"),
            )

        feature.name = new_feature_name
        feature.value = new_feature_value
        feature.save()

        return CustomResponse.success(
            message="The environment feature has been deleted successfully.",
            data=SwitchKeysFeatureSerializer(feature).data,
        )
