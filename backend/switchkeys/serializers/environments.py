from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    Serializer,
    CharField,
    IntegerField,
    BooleanField,
    ListField
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



class FeatureSerializer(Serializer):
    name = CharField()
    value = CharField()
    
class EnvironmentUserFeatureSerializer(Serializer):
    username = CharField()
    feature = FeatureSerializer()

class EnvironmentUserFeaturesSerializer(Serializer):
    username = CharField()
    features = ListField(child=FeatureSerializer())

class EnvironmentFeatureSerialize(ModelSerializer):

    environment = SerializerMethodField()

    class Meta:
        model = EnvironmentFeature
        fields = (
            "id",
            "created",
            "modified",
            "environment",
            "name",
            "value",
            "is_enabled",
            "is_default",
        )

        read_only_fields = (
            "id",
            "created",
            "modified",
        )

    def get_environment(self, obj: EnvironmentFeature):
        return ProjectEnvironmentSerializer(obj.environment).data


class UserFeatureSerialize(ModelSerializer):

    class Meta:
        model = EnvironmentFeature
        fields = (
            "id",
            "created",
            "modified",
            "name",
            "value",
        )

        read_only_fields = (
            "id",
            "created",
            "modified",
        )


class EnvironmentUserDeviceSerializer(Serializer):
    version = CharField()
    device_type = CharField()


class AddEnvironmentUserSerializer(Serializer):
    """Serializer to add user to an environment"""

    device = EnvironmentUserDeviceSerializer()
    username = CharField()

    class Meta:
        model = ProjectEnvironmentUser
        fields = (
            "username",
            "device",
        )

class AddEnvironmentUsersSerializer(Serializer):
    users = ListField(child = AddEnvironmentUserSerializer())

class RemoveEnvironmentUserSerializer(Serializer):
    """Serializer to remove user to an environment"""

    username = CharField()

class GetEnvironmentUserFeatureValueSerializer(Serializer):
    username = CharField()
    feature = CharField()
