from rest_framework.serializers import ModelSerializer, SerializerMethodField, Serializer, CharField

from switchkey.serializers.users import ProjectEnvironmentUserSerializer
from switchkey.serializers.projects import OrganizationProjectSerializer
from switchkey.models.management import EnvironmentFeature, ProjectEnvironment


class ProjectEnvironmentSerializer(ModelSerializer):
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


class SetEnvironmentSerializer(Serializer):
    key = CharField()
    value = CharField()

class EnvironmentFeatureSerialize(ModelSerializer):
    
    environment = SerializerMethodField()

    class Meta:
        model = EnvironmentFeature
        fields = (
            "id",
            "created",
            "modified",
            "environment",
            "key",
            "value",
            "tag",
            "tag_color",
            "description",
            "enabled_by_default",
            "is_default",
            "last_used",
        )

        read_only_fields = ("id", "created", "modified", "last_used", )

    def get_environment(self, obj: EnvironmentFeature):
        return ProjectEnvironmentSerializer(obj.environment).data