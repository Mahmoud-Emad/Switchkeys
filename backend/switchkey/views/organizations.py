from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from switchkey.serializers.organizations import OrganizationSerializer
from switchkey.services.organizations import (
    get_all_organization,
    get_organization_by_id,
)
from switchkey.api.custom_response import CustomResponse


class BaseOrganizationApiView(ListAPIView):
    serializer_class = OrganizationSerializer

    def get_queryset(self) -> Response:
        """Get all ``organization`` in the system"""
        get_queryset = get_all_organization()
        return get_queryset

    def post(self, request: Request) -> Response:
        """Create new organization object."""

        organization = request.data
        serializer = self.get_serializer(data=organization)
        if serializer.is_valid():
            serializer.save()
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
            serializer.save()
            return CustomResponse.success(
                data=serializer.data,
                message="Organization has been updated successfully.",
                status_code=201,
            )

        return CustomResponse.bad_request(
            data=OrganizationSerializer(organization).data,
            message="Please make sure that you entered a valid data..",
            error=serializer.errors,
        )

    def delete(self, request: Request, organization_id: str) -> Response:
        """Update organization by id"""
        organization = get_organization_by_id(organization_id)

        if organization is None:
            return CustomResponse.not_found(message="The organization does not exist.")

        organization.delete()
        return CustomResponse.success(
            data={},
            message="Organization has been updated successfully.",
            status_code=204,
        )
