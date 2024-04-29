from rest_framework.generics import ListAPIView
from rest_framework.request import Request

from switchkeys.services.projects import get_project_by_id
from switchkeys.models.management import OrganizationProject
from switchkeys.api.custom_response import CustomResponse
from switchkeys.services.environments import get_all_environments
from switchkeys.api.permissions import IsAdminUser, UserIsAuthenticated
from switchkeys.serializers.environments import ProjectEnvironmentSerializer

class BaseProjectEnvironmentApiView(ListAPIView):
    serializer_class = ProjectEnvironmentSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = []
        else:
            self.permission_classes = [
                IsAdminUser,
            ]

        return super(BaseProjectEnvironmentApiView, self).get_permissions()

    def get_queryset(self) -> CustomResponse:
        """Get all ``environments`` in the system."""
        get_queryset = get_all_environments()
        return get_queryset

    def post(self, request: Request) -> CustomResponse:
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
