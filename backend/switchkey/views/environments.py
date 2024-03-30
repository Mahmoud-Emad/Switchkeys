from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from switchkey.utils.validators import is_valid_uuid
from switchkey.services.environments import (
    get_all_environments,
    get_environment_by_id,
    get_environment_by_key,
)
from switchkey.models.management import OrganizationProject
from switchkey.serializers.environments import OrganizationProjectEnvironmentSerializer
from switchkey.api.permissions import UserIsAuthenticated, IsAdminUser
from switchkey.api.custom_response import CustomResponse


class BaseOrganizationProjectEnvironmentApiView(ListAPIView):
    serializer_class = OrganizationProjectEnvironmentSerializer
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
            project: OrganizationProject = serializer.validated_data.get("project")
            if request.user.id != project.organization.owner.id:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not the creator of the organization that owns this project.",
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


class OrganizationProjectEnvironmentApiView(GenericAPIView):
    serializer_class = OrganizationProjectEnvironmentSerializer
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

        return super(OrganizationProjectEnvironmentApiView, self).get_permissions()

    def get(self, request: Request, environment_id: str) -> Response:
        """Get an project environment by its ID."""
        environment = get_environment_by_id(environment_id)

        if environment is None:
            return CustomResponse.not_found(
                message="The project environment does not exist."
            )
        return CustomResponse.success(
            data=OrganizationProjectEnvironmentSerializer(environment).data,
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
            project: OrganizationProject = serializer.validated_data.get("project")
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
            data=OrganizationProjectEnvironmentSerializer(environment).data,
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
    serializer_class = OrganizationProjectEnvironmentSerializer

    def get(self, request: Request, environment_key: str):
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
            data=OrganizationProjectEnvironmentSerializer(environment).data,
        )
