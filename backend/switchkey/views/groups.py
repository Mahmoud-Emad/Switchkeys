from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from switchkey.models.management import OrganizationProject
from switchkey.serializers.groups import OrganizationProjectGroupSerializer
from switchkey.api.permissions import UserIsAuthenticated, IsAdminUser
from switchkey.services.groups import get_all_groups, get_group_by_id
from switchkey.api.custom_response import CustomResponse


class BaseOrganizationProjectGroupApiView(ListAPIView):
    serializer_class = OrganizationProjectGroupSerializer
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

        return super(BaseOrganizationProjectGroupApiView, self).get_permissions()

    def get_queryset(self) -> Response:
        """Get all ``groups`` in the system."""
        get_queryset = get_all_groups()
        return get_queryset

    def post(self, request: Request) -> Response:
        """Create new organization project group."""

        group = request.data
        serializer = self.get_serializer(data=group)
        if serializer.is_valid():
            project: OrganizationProject = serializer.validated_data.get("project")
            if request.user.id != project.organization.owner.id:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not the creator of the organization that owns this project.",
                )
            serializer.save()
            return CustomResponse.success(
                data=serializer.data,
                message="Organization project group has been created successfully.",
            )

        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
            data=request.data,
        )


class OrganizationProjectGroupApiView(GenericAPIView):
    serializer_class = OrganizationProjectGroupSerializer
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

        return super(OrganizationProjectGroupApiView, self).get_permissions()

    def get(self, request: Request, group_id: str) -> Response:
        """Get an organization project group by its ID."""
        group = get_group_by_id(group_id)

        if group is None:
            return CustomResponse.not_found(
                message="The organization project group does not exist."
            )
        return CustomResponse.success(
            data=OrganizationProjectGroupSerializer(group).data,
            message="The organization project found.",
        )

    def put(self, request: Request, group_id: str) -> Response:
        """Update an organization project group by its ID."""
        group = get_group_by_id(group_id)

        if group is None:
            return CustomResponse.not_found(
                message="The organization project group does not exist."
            )

        data = request.data
        serializer = self.get_serializer(group, data=data)
        if serializer.is_valid():
            project: OrganizationProject = serializer.validated_data.get("project")
            if request.user.id != project.organization.owner.id:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not the creator of the organization that owns this project.",
                )

            serializer.save()
            return CustomResponse.success(
                data=serializer.data,
                message="Organization project group has been updated successfully.",
                status_code=201,
            )

        return CustomResponse.bad_request(
            data=OrganizationProjectGroupSerializer(group).data,
            message="Please make sure that you entered a valid data..",
            error=serializer.errors,
        )

    def delete(self, request: Request, group_id: str) -> Response:
        """Delete an organization project group by its ID."""
        group = get_group_by_id(group_id)

        if group is None:
            return CustomResponse.not_found(
                message="The organization project does not exist."
            )

        project: OrganizationProject = group.project
        if request.user.id != project.organization.owner.id:
            return CustomResponse.unauthorized(
                message="You do not have permission to access this resource because you are not the creator of the organization that owns this project.",
            )

        group.delete()
        return CustomResponse.success(
            data={},
            message="Organization project has been updated successfully.",
            status_code=204,
        )
