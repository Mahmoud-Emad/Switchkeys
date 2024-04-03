from uuid import UUID
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from switchkeys.services.projects import get_project_by_id
from switchkeys.utils.validators import is_valid_uuid
from switchkeys.services.environments import (
    create_environment_user,
    get_all_environment_features,
    get_all_environments,
    get_environment_by_id,
    get_environment_by_key,
    get_environment_user_by_id,
    get_environment_user_username,
)
from switchkeys.models.management import OrganizationProject, ProjectEnvironment
from switchkeys.serializers.environments import (
    AddEnvironmentUserSerializer,
    EnvironmentFeatureSerialize,
    ProjectEnvironmentSerializer,
    RemoveEnvironmentUserSerializer,
    SetEnvironmentSerializer,
)
from switchkeys.api.permissions import UserIsAuthenticated, IsAdminUser
from switchkeys.api.custom_response import CustomResponse


class BaseOrganizationProjectEnvironmentApiView(ListAPIView):
    serializer_class = ProjectEnvironmentSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                UserIsAuthenticated,
            ]
        else:
            self.permission_classes = [
                IsAdminUser,
            ]

        return super(BaseOrganizationProjectEnvironmentApiView, self).get_permissions()

    def get_queryset(self) -> Response:
        """Get all ``environments`` in the system."""
        get_queryset = get_all_environments()
        return get_queryset

    def post(self, request: Request) -> Response:
        """Create new project environment."""

        environment = request.data
        serializer = self.get_serializer(data=environment)
        if serializer.is_valid():
            project_id: int = serializer.validated_data.get("project_id")
            project: OrganizationProject = get_project_by_id(str(project_id))

            if project is None:
                return CustomResponse.not_found(
                    message="Project not found.",
                )

            if request.user.id != project.organization.owner.id:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not the creator of the organization that owns this project.",
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


class OrganizationProjectEnvironmentApiView(GenericAPIView):
    serializer_class = ProjectEnvironmentSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = []
        else:
            self.permission_classes = [
                IsAdminUser,
            ]

        return super(OrganizationProjectEnvironmentApiView, self).get_permissions()

    def get(self, request: Request, environment_id: str) -> Response:
        """Get an project environment by its ID."""
        environment = get_environment_by_id(environment_id)

        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )
        return CustomResponse.success(
            data=ProjectEnvironmentSerializer(environment).data,
            message="The project environment found.",
        )

    def put(self, request: Request, environment_id: str) -> Response:
        """Update an project environment by its ID."""
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
                return CustomResponse.not_found(
                    message="Project not found.",
                )

            if request.user.id != project.organization.owner.id:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not the creator of the organization that owns this project.",
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

    def delete(self, request: Request, environment_id: str) -> Response:
        """Delete an project environment by its ID."""
        environment = get_environment_by_id(environment_id)

        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        project: OrganizationProject = environment.project
        if request.user.id != project.organization.owner.id:
            return CustomResponse.unauthorized(
                message="You do not have permission to access this resource because you are not the creator of the organization that owns this project.",
            )

        environment.delete()
        return CustomResponse.success(
            data={},
            message="Project has been updated successfully.",
            status_code=204,
        )


class OrganizationProjectEnvironmentKeyApiView(GenericAPIView):
    serializer_class = ProjectEnvironmentSerializer

    def get(self, request: Request, environment_key: UUID):
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
            data=ProjectEnvironmentSerializer(environment).data,
        )


class SetEnvironmentKeyApiView(GenericAPIView):
    serializer_class = SetEnvironmentSerializer

    def post(self, request: Request, environment_key: UUID):
        if not is_valid_uuid(environment_key):
            return CustomResponse.bad_request(
                message=f"{environment_key} is not valid UUID."
            )

        if not request.query_params.get("user_id"):
            return CustomResponse.bad_request(
                message="You have to send the `user_id` as a query params."
            )

        environment = get_environment_by_key(environment_key)
        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        user_id = request.query_params.get("user_id")
        environment_user = get_environment_user_by_id(user_id)

        if environment_user is None:
            return CustomResponse.not_found(
                message="The environment user does not exist."
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            key = serializer.validated_data.get("key")
            value = serializer.validated_data.get("value")
            environment_user.features[key] = {"value": value, "is_enabled": True}
            environment_user.save()
            return CustomResponse.success(
                message="The user features has been updated.",
                data=environment_user.features,
            )
        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
        )


class BaseEnvironmentFeatureAPIView(ListAPIView):

    serializer_class = EnvironmentFeatureSerialize
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = []
        else:
            self.permission_classes = [UserIsAuthenticated]

        return super(BaseEnvironmentFeatureAPIView, self).get_permissions()

    def get_queryset(self) -> Response:
        """Get all ``environment features`` in the system."""
        get_queryset = get_all_environment_features()
        return get_queryset

    def post(self, request: Request) -> Response:
        """Create new project environment."""

        feature = request.data
        serializer = self.get_serializer(data=feature)
        if serializer.is_valid():
            environment: ProjectEnvironment = serializer.validated_data.get(
                "environment"
            )
            if request.user.id not in environment.project.organization.members:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not a member in organization that owns this project.",
                )
            serializer.save()
            return CustomResponse.success(
                data=serializer.data,
                message="Project environment has been created successfully.",
            )

        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
            data=request.data,
        )


class AddEnvironmentUserAPIView(GenericAPIView):
    serializer_class = AddEnvironmentUserSerializer
    permission_classes = [IsAdminUser]

    def put(self, request: Request, environment_key: str):
        environment = get_environment_by_key(environment_key)
        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            user = get_environment_user_username(username)
            if user is None:
                device_type = serializer.validated_data.get('device').get("device_type")
                device_version = serializer.validated_data.get('device').get("version")
                features = serializer.validated_data.get('features')

                user = create_environment_user(
                    username=username,
                    device_type=device_type,
                    device_version=device_version,
                    features=features
                )

            environment.users.add(user)
            environment.save()
            return CustomResponse.success(message="User added successfully.", data=AddEnvironmentUserSerializer(user).data)
        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
        )

class RemoveEnvironmentUserAPIView(GenericAPIView):
    serializer_class = RemoveEnvironmentUserSerializer
    permission_classes = [IsAdminUser]

    def put(self, request: Request, environment_key: str):
        environment = get_environment_by_key(environment_key)
        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            user = get_environment_user_username(username)
            if user is None:
                return CustomResponse.not_found(message="User not found.")

            environment.users.remove(user)
            environment.save()
            return CustomResponse.success(message="User removed successfully.", data=AddEnvironmentUserSerializer(user).data)
        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
        )


class EnvironmentFeatureAPIView(GenericAPIView):
    pass
