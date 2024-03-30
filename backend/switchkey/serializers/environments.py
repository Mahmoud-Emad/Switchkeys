from rest_framework.serializers import ModelSerializer, SerializerMethodField

from switchkey.serializers.users import ProjectEnvironmentUserSerializer
from switchkey.serializers.projects import OrganizationProjectSerializer
from switchkey.models.management import ProjectEnvironment


class OrganizationProjectEnvironmentSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization project environment`` .
    """

    project = SerializerMethodField()
    users = SerializerMethodField()

    class Meta:
        model = ProjectEnvironment
        fields = (
            "id",
            "name",
            "created",
            "modified",
            "project",
            "environment_key",
            "users",
        )
        read_only_fields = ("id", "created", "modified", "environment_key")

    def get_project(self, obj: ProjectEnvironment):
        return OrganizationProjectSerializer(obj.project).data

    def get_users(self, obj: ProjectEnvironment):
        return ProjectEnvironmentUserSerializer(obj.users, many=True).data
