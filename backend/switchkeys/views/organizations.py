from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from switchkeys.services.users import get_user_by_id
from switchkeys.api.permissions import UserIsAuthenticated, IsAdminUser
from switchkeys.serializers.organizations import OrganizationAddMemberSerializer, OrganizationSerializer
from switchkeys.services.organizations import (
    check_organization_name,
    get_all_organization,
    get_organization_by_id,
    get_user_organization_by_name,
)
from switchkeys.api.custom_response import CustomResponse


class BaseOrganizationApiView(ListAPIView):
    serializer_class = OrganizationSerializer
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

        return super(BaseOrganizationApiView, self).get_permissions()

    def get_queryset(self) -> Response:
        """Get all ``organization`` in the system"""
        get_queryset = get_all_organization()
        return get_queryset

    def post(self, request: Request) -> Response:
        """Create new organization object."""

        organization = request.data
        serializer = self.get_serializer(data=organization)
        if serializer.is_valid():
            # Check if there an organization created by the requested user with the same name
            organization_name = serializer.validated_data.get("name")
            created = check_organization_name(request.user, organization_name)
            if created:
                return CustomResponse.bad_request(
                    message="An organization with the same name has already been created by this user."
                )

            organization_members = request.data.get("members")

            if type(organization_members) is list and len(organization_members) >= 0:
                serializer.save(owner=request.user, members=organization_members)
            else:
                serializer.save(owner=request.user)

            return CustomResponse.success(
                data=serializer.data,
                message="Organization has been created successfully.",
            )

        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
            data=request.data,
        )


class OrganizationApiView(GenericAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = []
        else:
            self.permission_classes = [
                IsAdminUser,
            ]

        return super(OrganizationApiView, self).get_permissions()

    def get(self, request: Request, organization_id: str) -> Response:
        """Get organization by id"""
        organization = get_organization_by_id(organization_id)

        if organization is None:
            return CustomResponse.not_found(message="The organization does not exist.")
        return CustomResponse.success(
            data=OrganizationSerializer(organization).data,
            message="The organization found.",
        )

    def put(self, request: Request, organization_id: str) -> Response:
        """Update organization by id"""
        organization = get_organization_by_id(organization_id)

        if organization is None:
            return CustomResponse.not_found(message="The organization does not exist.")

        data = request.data
        serializer = self.get_serializer(organization, data=data)
        if serializer.is_valid():
            # Check if there an organization created by the requested user with the same name
            organization_name = serializer.validated_data.get("name")
            created = check_organization_name(request.user, organization_name)
            if created:
                return CustomResponse.bad_request(
                    message="An organization with the same name has already been created by this user."
                )

            organization_members = request.data.get("members")

            if type(organization_members) is list and len(organization_members) >= 0:
                serializer.save(owner=request.user, members=organization_members)
            else:
                serializer.save(owner=request.user)

            return CustomResponse.success(
                data=serializer.data,
                message="Organization has been updated successfully.",
                status_code=201,
            )

        return CustomResponse.bad_request(
            data=request.data,
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
        )

    def delete(self, request: Request, organization_id: str) -> Response:
        """Delete an organization by its ID."""
        organization = get_organization_by_id(organization_id)

        if organization is None:
            return CustomResponse.not_found(message="The organization does not exist.")

        organization.delete()

        return CustomResponse.success(
            message="Organization has been deleted successfully.",
            status_code=204,
        )


class OrganizationByNameApiView(GenericAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [
        UserIsAuthenticated,
    ]

    def get(self, request: Request, organization_name: str) -> Response:
        """
        Get organization by name, use this endpoint if you want to
        """
        organization = get_user_organization_by_name(request.user, organization_name)

        if organization is None:
            return CustomResponse.not_found(message="The organization does not exist.")
        return CustomResponse.success(
            data=OrganizationSerializer(organization).data,
            message="The organization found.",
        )

class OrganizationAddMemberApiView(GenericAPIView):
    serializer_class = OrganizationAddMemberSerializer
    permission_classes = [
        IsAdminUser,
    ]
    
    def put(self, request: Request, organization_id: str) -> Response:
        """
            Add a member on an organization
        """

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            
            organization = get_organization_by_id(organization_id)
            if organization is None:
                return CustomResponse.not_found(message="The organization does not exist.")

            member_id = serializer.validated_data.get("member_id")
            member = get_user_by_id(member_id)
            if member is None:
                return CustomResponse.not_found(message="The member does not exist.")

            organization.members.add(member)
            organization.save()

            return CustomResponse.success(
                data=OrganizationSerializer(organization).data,
                message="The member has been added to the organization.",
            )

        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
            data=request.data
        )

class OrganizationRemoveMemberApiView(GenericAPIView):
    serializer_class = OrganizationAddMemberSerializer
    permission_classes = [
        IsAdminUser,
    ]
    
    def put(self, request: Request, organization_id: str) -> Response:
        """
            Add a member on an organization
        """

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            
            organization = get_organization_by_id(organization_id)
            if organization is None:
                return CustomResponse.not_found(message="The organization does not exist.")

            member_id = serializer.validated_data.get("member_id")
            member = get_user_by_id(member_id)
            if member is None:
                return CustomResponse.not_found(message="The member does not exist.")

            if member not in organization.members.all():
                return CustomResponse.bad_request(
                    data=request.data,
                    message=f"Member with ID `{member_id}` is not registered as a member of the organization named `{organization.name}`.",
                )
 
            organization.members.remove(member)
            organization.save()

            return CustomResponse.success(
                data=OrganizationSerializer(organization).data,
                message="The member has been added to the organization.",
            )

        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
            data=request.data
        )
