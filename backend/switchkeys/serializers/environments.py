from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    SerializerMethodField,
    IntegerField,
    CharField,
)

from switchkeys.serializers.users import ProjectEnvironmentUserSerializer
from switchkeys.models.management import ProjectEnvironment
from switchkeys.models.environments import EnvironmentFeature, SwitchKeysFeature, UserFeature

class EnvironmentUserDeviceSerializer(Serializer):
    version = CharField()
    device_type = CharField()

class ProjectEnvironmentSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization project environment`` .
    """

    project = SerializerMethodField()
    users = SerializerMethodField()
    features = SerializerMethodField()

    class Meta:
        model = ProjectEnvironment
        fields = (
            "id",
            "name",
            "created",
            "modified",
            "environment_key",
            "features",
            "project",
            "users",
        )

        read_only_fields = ("id", "created", "modified", "environment_key")

    def get_project(self, obj: ProjectEnvironment):
        from switchkeys.serializers.projects import OrganizationProjectSerializer

        return OrganizationProjectSerializer(obj.project).data

    def get_users(self, obj: ProjectEnvironment):
        return ProjectEnvironmentUserSerializer(obj.users, many=True).data

    def get_features(self, obj: ProjectEnvironment):
        features = EnvironmentFeature.objects.filter(environment=obj)
        serialized_features = []

        for feature in features:
            serialized_features.extend(
                EnvironmentFeatureSerializer(feature.features.all(), many=True).data
            )
        
        return serialized_features

class EnvironmentFeatureSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = SwitchKeysFeature
