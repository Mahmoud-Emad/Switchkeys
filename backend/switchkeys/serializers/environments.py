from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    Serializer,
    CharField,
    IntegerField,
)

from switchkeys.models.users import ProjectEnvironmentUser
from switchkeys.serializers.users import ProjectEnvironmentUserSerializer
from switchkeys.serializers.projects import OrganizationProjectSerializer
from switchkeys.models.management import EnvironmentFeature, ProjectEnvironment


class ProjectEnvironmentSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization project environment`` .
    """

    project_id = IntegerField()
    project = SerializerMethodField()
    users = SerializerMethodField()

    class Meta:
        model = ProjectEnvironment
        fields = (
            "id",
            "name",
            "project_id",
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

        read_only_fields = (
            "id",
            "created",
            "modified",
            "last_used",
        )

    def get_environment(self, obj: EnvironmentFeature):
        return ProjectEnvironmentSerializer(obj.environment).data


class EnvironmentUserDeviceSerializer(Serializer):
    version = CharField()
    device_type = CharField()


class AddEnvironmentUserSerializer(ModelSerializer):
    """Serializer to add user to an environment"""
    device = EnvironmentUserDeviceSerializer()

    class Meta:
        model = ProjectEnvironmentUser
        fields = (
            "id",
            "created",
            "modified",
            "username",
            "device",
            "features",
        )

        read_only_fields = (
            "id",
            "created",
            "modified",
        )
