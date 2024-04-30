from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.request import Request
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
    get_all_environments,
    get_environment_by_id,
    get_environment_by_key,
    get_environment_user_username,
    validate_unique_environment_name,
)
from switchkeys.api.permissions import (
    HasEnvironmentKey,
    IsAdminUser,
    UserIsAuthenticated,
)
from switchkeys.serializers.environments import (
    AddEnvironmentUserSerializer,
    ProjectEnvironmentSerializer,
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
            data={},
            message="Project has been updated successfully.",
            status_code=204,
        )


class AddEnvironmentUserAPIView(GenericAPIView):
    """
    API endpoint for adding a user to an environment.
    """

    serializer_class = AddEnvironmentUserSerializer

    def put(self, request: Request, environment_key: str) -> CustomResponse:
        """
        Adds a user to the specified environment.
        """
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
            environment_features = EnvironmentFeature.objects.get(
                environment=environment
            )

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
                        feature_value=feature.value
                    )

            environment.save()
            return CustomResponse.success(
                message="User added successfully.", data=serializer.data
            )
        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
        )
